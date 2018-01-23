import sys
from time import sleep

import RPi.GPIO as GPIO

from robot.MotorController import MotorController
from robot.Robot import Robot


def main() -> None:
    GPIO.setmode(GPIO.BCM)

    robot = Robot(MotorController.DRIVING_DIRECTION_STRAIGHT)
    robot.start()

    # Keep the program running so we can listen for the button event
    while True:
        sleep(0.01)


# Make the program easy to run
if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        GPIO.cleanup()
        sys.exit(0)
