import sys
from time import sleep

import RPi.GPIO as GPIO

from robot.Button import Button
from robot.Motor import Motor
from robot.Pins import Pins


def on_button_click(channel):
    motor = Motor(Pins["MOTOR_LEFT_PIN_1"],
                  Pins["MOTOR_LEFT_PIN_2"],
                  Pins["MOTOR_LEFT_PIN_3"],
                  Pins["MOTOR_LEFT_PIN_4"])

    motor.rotate(100)


def main():
    GPIO.setmode(GPIO.BCM)

    button = Button(Pins["BUTTON"], on_button_click).listen()

    while True:
        sleep(0.01)


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        GPIO.cleanup()
        sys.exit(0)
