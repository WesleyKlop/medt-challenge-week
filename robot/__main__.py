import sys
from time import sleep

import RPi.GPIO as GPIO

from robot.Button import Button
from robot.Motor import Motor
from robot.MotorController import MotorController
from robot.Pins import Pins

motor_controller = None


def on_button_click(channel):
    global motor_controller
    motor_controller.drive_forward(1000)
    sys.exit(0)


def main():
    global motor_controller
    GPIO.setmode(GPIO.BCM)

    button = Button(Pins["BUTTON"], on_button_click).listen()
    left_motor = Motor(Pins["MOTOR_LEFT_PIN_1"],
                       Pins["MOTOR_LEFT_PIN_2"],
                       Pins["MOTOR_LEFT_PIN_3"],
                       Pins["MOTOR_LEFT_PIN_4"])
    right_motor = Motor(Pins["MOTOR_RIGHT_PIN_1"],
                        Pins["MOTOR_RIGHT_PIN_2"],
                        Pins["MOTOR_RIGHT_PIN_3"],
                        Pins["MOTOR_RIGHT_PIN_4"])
    motor_controller = MotorController(left_motor, right_motor)

    while True:
        sleep(0.01)


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        GPIO.cleanup()
        sys.exit(0)
