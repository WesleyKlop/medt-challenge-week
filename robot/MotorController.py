from time import sleep

from robot.Motor import Motor


class MotorController:
    def __init__(self, left_motor, right_motor):
        self.left_motor = left_motor
        self.right_motor = right_motor

    def drive_forward(self, times: int = 1) -> None:
        for i in range(times):
            for activePin in range(0, 4):
                self.left_motor.step(activePin)
                self.right_motor.step(activePin)
                sleep(Motor.delay)
