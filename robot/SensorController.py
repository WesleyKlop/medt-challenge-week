from time import time

import numpy as np

from robot.Log import log
from robot.MotorController import MotorController
from robot.Sensor import Sensor


class SensorController:
    SENSOR_WHITE = 1
    SENSOR_BLACK = 0
    LOCK_TIME = 800

    def __init__(self, left_sensor_pin: int, middle_sensor_pin: int, right_sensor_pin: int, change_driving_direction,
                 on_destination_reached: callable):
        self.left_sensor = Sensor(left_sensor_pin, self.on_sensor_change).listen()
        self.right_sensor = Sensor(right_sensor_pin, self.on_sensor_change).listen()
        self.middle_sensor = Sensor(middle_sensor_pin, self.on_sensor_change).listen()
        self.callback = change_driving_direction
        self.prev_state = [1, 0, 1]
        self.prev_direction = MotorController.DRIVING_DIRECTION_STRAIGHT
        self.direction_locked = 0
        self.found_intersection = False
        self.destination = None  # type: str
        self.on_destination_reached = on_destination_reached

    def reset(self):
        """Reset SensorController"""
        self.left_sensor.reset()
        self.middle_sensor.reset()
        self.right_sensor.reset()
        self.prev_state = [1, 0, 1]
        self.destination = None
        self.found_intersection = False
        self.direction_locked = 0
        self.prev_direction = MotorController.DRIVING_DIRECTION_STRAIGHT

    def get_sensor_state(self):
        """Return current sensor state"""
        return [
            self.left_sensor.get_state(),
            self.middle_sensor.get_state(),
            self.right_sensor.get_state()
        ]

    def change_driving_direction(self, direction: str, tight: bool = False):
        """Change the driving direction when nog locked"""
        if int(time() * 1000) - self.direction_locked > SensorController.LOCK_TIME:
            self.prev_direction = direction
            log.write(direction)
            self.callback(direction, tight)
            self.direction_locked = 0

    def lock_direction(self, lock_time: int = 800):
        """Lock the direction we're going in for x amount of ms"""
        self.direction_locked = int(time() * 1000)
        print(self.direction_locked)
        SensorController.LOCK_TIME = lock_time

    def on_sensor_change(self, _):
        """Check all available combinations to see what direction we need to go"""
        sensor_state = self.get_sensor_state()
        if np.array_equal(sensor_state, [1, 1, 0]) or np.array_equal(sensor_state, [1, 0, 0]):
            self.change_driving_direction(MotorController.DRIVING_DIRECTION_RIGHT)
        elif np.array_equal(sensor_state, [0, 0, 1]) or np.array_equal(sensor_state, [0, 1, 1]):
            self.change_driving_direction(MotorController.DRIVING_DIRECTION_LEFT)
        elif np.array_equal(sensor_state, [1, 0, 1]):
            if np.array_equal(self.prev_state, [0, 0, 0]):
                print("Encountered an intersection, driving backwards as a check")
                self.change_driving_direction(MotorController.DRIVING_DIRECTION_BACKWARDS)
            else:
                self.change_driving_direction(MotorController.DRIVING_DIRECTION_STRAIGHT)
        elif np.array_equal(sensor_state, [0, 0, 0]):
            # When we encounter all black while we we're driving backwards we found an intersection.
            log.write("INTERSECTION")
            if self.found_intersection:
                log.write("FINISHED")
                self.change_driving_direction(MotorController.DRIVING_DIRECTION_STOP)
                self.on_destination_reached()
            else:
                log.write("INTERSECTION {}".format(self.destination))
                self.change_driving_direction(self.destination, True)
                self.found_intersection = True
                self.lock_direction(1000)
        elif np.array_equal(sensor_state, [1, 1, 1]):
            # When the robot encounters only white surface check if the previous state was cornering,
            # if that is true than take the corner tighter defined by the "True" argument
            if np.array_equal(self.prev_state, [1, 0, 0]) or np.array_equal(self.prev_state, [1, 1, 0]):
                self.change_driving_direction(MotorController.DRIVING_DIRECTION_RIGHT, True)
            elif np.array_equal(self.prev_state, [0, 0, 1]) or np.array_equal(self.prev_state, [0, 1, 1]):
                self.change_driving_direction(MotorController.DRIVING_DIRECTION_LEFT, True)
            elif np.array_equal(self.prev_state, [1, 0, 1]):
                # This is probably a dashed line, just keep driving (probably doesn't work for level 6)
                self.change_driving_direction(MotorController.DRIVING_DIRECTION_STRAIGHT)
            elif np.array_equal(self.prev_state, [0, 0, 0]):
                # We reached an ending
                self.change_driving_direction(MotorController.DRIVING_DIRECTION_STOP)
        self.prev_state = sensor_state
