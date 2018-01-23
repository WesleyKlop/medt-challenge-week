from time import sleep

from robot.Motor import Motor


class MotorController:
    DRIVING_DIRECTION_STRAIGHT = "STRAIGHT"
    DRIVING_DIRECTION_LEFT = "LEFT"
    DRIVING_DIRECTION_RIGHT = "RIGHT"
    DRIVING_DIRECTION_BACKWARDS = "BACKWARDS"

    def __init__(self, left_motor: Motor, right_motor: Motor):
        self.driving_direction = MotorController.DRIVING_DIRECTION_BACKWARDS
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
        for i in range(times):
            for active_pin in range(0, 4):
                self.left_motor.step(active_pin)
            for active_pin in reversed(range(0, 4)):
                self.right_motor.step(active_pin)
            sleep(Motor.delay)

    def drive_left(self, times: int = 1) -> None:
        """Drive left for {times} loops"""
        for i in range(times):
            self.right_motor.step(0)
            self.left_motor.step(3)
            self.right_motor.step(1)
            self.left_motor.step(2)
            self.right_motor.step(2)
            self.left_motor.step(1)
            self.right_motor.step(3)
            self.left_motor.step(0)
            sleep(Motor.delay)

    def drive_backwards(self, times: int = 1) -> None:
        """Drive forward for {times} loops"""
        for i in range(times):
            self.right_motor.step(3)
            self.left_motor.step(3)
            self.right_motor.step(2)
            self.left_motor.step(2)
            self.right_motor.step(1)
            self.left_motor.step(1)
            self.right_motor.step(0)
            self.left_motor.step(0)
            # for active_pin in reversed(range(0, 4)):
            #     self.left_motor.step(active_pin)
            #     self.right_motor.step(active_pin)
            sleep(Motor.delay)

    def drive(self) -> None:
        """Keep following the black line"""
        while True:
            print(self.driving_direction)
            if self.driving_direction == MotorController.DRIVING_DIRECTION_STRAIGHT:
                self.drive_straight(4)
            elif self.driving_direction == MotorController.DRIVING_DIRECTION_LEFT:
                self.drive_left(4)
            elif self.driving_direction == MotorController.DRIVING_DIRECTION_RIGHT:
                self.drive_right(4)
            elif self.driving_direction == MotorController.DRIVING_DIRECTION_BACKWARDS:
                self.drive_backwards(4)
