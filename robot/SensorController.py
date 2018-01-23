import RPi.GPIO as GPIO
import numpy as np

from robot.MotorController import MotorController
from robot.Sensor import Sensor


class SensorController:
    SENSOR_WHITE = 1
    SENSOR_BLACK = 0

    def __init__(self, left_sensor_pin: int, middle_sensor_pin: int, right_sensor_pin: int, callback: callable(str)):
        self.left_sensor = Sensor(left_sensor_pin, self.on_sensor_change).listen()
        self.right_sensor = Sensor(right_sensor_pin, self.on_sensor_change).listen()
        self.middle_sensor = Sensor(middle_sensor_pin, self.on_sensor_change).listen()
        self.callback = callback
        self.pins = {
            "left": left_sensor_pin,
            "middle": middle_sensor_pin,
            "right": right_sensor_pin,
        }

    def get_sensor_state(self):
        return [
            GPIO.input(self.pins["left"]),
            GPIO.input(self.pins["middle"]),
            GPIO.input(self.pins["right"])
        ]

    def on_sensor_change(self, channel):
        """Check all available combinations to see what direction we need to go"""
        sensor_state = self.get_sensor_state()
        print(sensor_state)
        if np.array_equal(sensor_state, [1, 0, 0]) or np.array_equal(sensor_state, [1, 1, 0]):
            self.callback(MotorController.DRIVING_DIRECTION_RIGHT)
        elif np.array_equal(sensor_state, [0, 0, 1]) or np.array_equal(sensor_state, [0, 1, 1]):
            self.callback(MotorController.DRIVING_DIRECTION_LEFT)
        elif np.array_equal(sensor_state, [1, 0, 1]):
            self.callback(MotorController.DRIVING_DIRECTION_STRAIGHT)
