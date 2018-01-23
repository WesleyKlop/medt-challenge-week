from time import sleep

from robot.Motor import Motor


class MotorController:
    def __init__(self, left_motor: Motor, right_motor: Motor):
        self.left_motor = left_motor
        self.right_motor = right_motor

    def drive_forward(self, times: int = 1) -> None:
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
