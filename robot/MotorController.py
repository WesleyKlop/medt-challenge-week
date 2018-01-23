from time import sleep

from robot.Motor import Motor


class MotorController:
    SENSOR_WHITE = 1
    SENSOR_BLACK = 0
    DRIVING_DIRECTION_STRAIGHT = "STRAIGHT"
    DRIVING_DIRECTION_LEFT = "LEFT"
    DRIVING_DIRECTION_RIGHT = "RIGHT"

    def __init__(self, left_motor: Motor, right_motor: Motor):
        self.driving_direction = MotorController.DRIVING_DIRECTION_STRAIGHT
        self.left_motor = left_motor
        self.right_motor = right_motor

    def drive_straight(self, times: int = 1) -> None:
        """Drive forward for {times} loops"""
        for i in range(times):
            for active_pin in range(0, 4):
                self.left_motor.step(active_pin)
                self.right_motor.step(active_pin)
                sleep(Motor.delay)

    def drive_right(self, times: int = 1) -> None:
        """Drive right for {times} loops"""
        self.left_motor.rotate(times)

    def drive_left(self, times: int = 1) -> None:
        """Drive left for {times} loops"""
        self.right_motor.rotate(times)

    def drive(self) -> None:
        """Keep following the black line"""
        while True:
            if self.driving_direction == MotorController.DRIVING_DIRECTION_STRAIGHT:
                self.drive_straight(4)
            elif self.driving_direction == MotorController.DRIVING_DIRECTION_LEFT:
                self.drive_left(4)
            elif self.driving_direction == MotorController.DRIVING_DIRECTION_RIGHT:
                self.drive_right(4)

    def on_left_sensor_change(self, state: int) -> None:
        if state == MotorController.SENSOR_BLACK:
            self.driving_direction = MotorController.DRIVING_DIRECTION_LEFT

    def on_right_sensor_change(self, state: int) -> None:
        if state == MotorController.SENSOR_BLACK:
            self.driving_direction = MotorController.DRIVING_DIRECTION_RIGHT
