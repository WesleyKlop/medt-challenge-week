import sys
from threading import Thread
from time import sleep

import RPi.GPIO as GPIO

from robot.Button import Button
from robot.Motor import Motor
from robot.MotorController import MotorController
from robot.Pins import Pins
from robot.Sensor import Sensor

motor_controller = None  # type: MotorController


def on_sensor_change(channel: int) -> None:
    global motor_controller
    if channel == Pins["SENSOR_LEFT"]:
        motor_controller.on_left_sensor_change(GPIO.input(channel))
        print("Left sensor is now {}".format(GPIO.input(channel)))
    elif channel == Pins["SENSOR_MIDDLE"]:
        print("Middle sensor is now {}".format(GPIO.input(channel)))
    elif channel == Pins["SENSOR_RIGHT"]:
        motor_controller.on_right_sensor_change(GPIO.input(channel))
        print("Right sensor is now {}".format(GPIO.input(channel)))


def on_button_click(channel: int) -> None:
    global motor_controller
    print("Button clicked!")
    drive_thread = Thread(target=motor_controller.drive, name="drive_thread")
    drive_thread.start()


def main() -> None:
    """Main method"""
    global motor_controller
    GPIO.setmode(GPIO.BCM)

    middle_sensor = Sensor(Pins["SENSOR_MIDDLE"], on_sensor_change).listen()
    left_sensor = Sensor(Pins["SENSOR_LEFT"], on_sensor_change).listen()
    right_sensor = Sensor(Pins["SENSOR_RIGHT"], on_sensor_change).listen()

    button = Button(Pins["BUTTON"], on_button_click).listen()

    motor_controller = MotorController(
        Motor(Pins["MOTOR_LEFT_PIN_1"],
              Pins["MOTOR_LEFT_PIN_2"],
              Pins["MOTOR_LEFT_PIN_3"],
              Pins["MOTOR_LEFT_PIN_4"]),
        Motor(Pins["MOTOR_RIGHT_PIN_1"],
              Pins["MOTOR_RIGHT_PIN_2"],
              Pins["MOTOR_RIGHT_PIN_3"],
              Pins["MOTOR_RIGHT_PIN_4"])
    )

    # Keep the program running
    while True:
        sleep(0.01)


# Make the program easy to run
if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        GPIO.cleanup()
        sys.exit(0)
