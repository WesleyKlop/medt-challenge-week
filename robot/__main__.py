import sys
from time import sleep

import RPi.GPIO as GPIO

from robot.Robot import Robot


def on_destination_reached():
    print("Destination reached!")
    GPIO.cleanup()
    sys.exit(0)


def main() -> None:
    GPIO.setmode(GPIO.BCM)

    robot = Robot(on_destination_reached)
    robot.start(auto_start=False)

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
