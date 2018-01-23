from time import sleep

from robot.Motor import Motor


class MotorController:
    DRIVING_DIRECTION_STRAIGHT = "STRAIGHT"
    DRIVING_DIRECTION_LEFT = "LEFT"
    DRIVING_DIRECTION_RIGHT = "RIGHT"
    DRIVING_DIRECTION_BACKWARDS = "BACKWARDS"
    DRIVING_DIRECTION_STOP = "STOP"

    def __init__(self, left_motor: Motor, right_motor: Motor, default_direction: str):
        self.driving_direction = default_direction
        self.left_motor = left_motor
        self.right_motor = right_motor
        self.tight_corner = False

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
                if self.tight_corner:
                    self.right_motor.step_backwards(active_pin)
                self.left_motor.step(active_pin)
                sleep(Motor.delay)

    def drive_left(self, times: int = 1) -> None:
        """Drive left for {times} loops"""
        for i in range(times):
            for active_pin in range(0, 4):
                self.right_motor.step(active_pin)
                if self.tight_corner:
                    self.left_motor.step_backwards(active_pin)
                sleep(Motor.delay)

    def drive_backwards(self, times: int = 1) -> None:
        """Drive forward for {times} loops"""
        for i in range(times):
            for active_pin in reversed(range(0, 4)):
                self.left_motor.step(active_pin)
                self.right_motor.step(active_pin)
            sleep(Motor.delay)

    def drive(self) -> None:
        """Keep following the black line"""
        while True:
            if self.driving_direction == MotorController.DRIVING_DIRECTION_STRAIGHT:
                self.drive_straight()
            elif self.driving_direction == MotorController.DRIVING_DIRECTION_LEFT:
                self.drive_left()
            elif self.driving_direction == MotorController.DRIVING_DIRECTION_RIGHT:
                self.drive_right()
            elif self.driving_direction == MotorController.DRIVING_DIRECTION_BACKWARDS:
                self.drive_backwards()
