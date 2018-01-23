import sys

import RPi.GPIO as GPIO

from robot.Button import Button
from robot.Motor import Motor
from robot.Pins import Pins

program_running = True
left_motor = None


def on_button_click(channel):
    global program_running, left_motor
    print("Clicked", channel)

    left_motor.rotate(100)

    program_running = False


def main():
    global program_running, left_motor
    GPIO.setmode(GPIO.BCM)

    button = Button(Pins["BUTTON"], on_button_click).listen()
    left_motor = Motor(Pins["MOTOR_LEFT_PIN_1"],
                       Pins["MOTOR_LEFT_PIN_2"],
                       Pins["MOTOR_LEFT_PIN_3"],
                       Pins["MOTOR_LEFT_PIN_4"])

    button.emulate_click()

    GPIO.cleanup()


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        GPIO.cleanup()
        sys.exit(0)
