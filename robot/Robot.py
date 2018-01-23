from threading import Thread

from robot.Button import Button
from robot.Motor import Motor
from robot.MotorController import MotorController
from robot.Pins import Pins
from robot.SensorController import SensorController


class Robot:

    def __init__(self, default_direction: str = MotorController.DRIVING_DIRECTION_STRAIGHT):
        self.drive_thread = None  # type: Thread

        left_motor = Motor(
            Pins["MOTOR_LEFT_PIN_1"],
            Pins["MOTOR_LEFT_PIN_2"],
            Pins["MOTOR_LEFT_PIN_3"],
            Pins["MOTOR_LEFT_PIN_4"])
        right_motor = Motor(
            Pins["MOTOR_RIGHT_PIN_1"],
            Pins["MOTOR_RIGHT_PIN_2"],
            Pins["MOTOR_RIGHT_PIN_3"],
            Pins["MOTOR_RIGHT_PIN_4"])
        self.motor_controller = MotorController(
            left_motor,
            right_motor,
            default_direction)

        self.sensor_controller = SensorController(
            Pins["SENSOR_LEFT"],
            Pins["SENSOR_MIDDLE"],
            Pins["SENSOR_RIGHT"],
            self.on_sensor_change)

        self.button = Button(Pins["BUTTON"], self.on_button_click)

    def on_sensor_change(self, direction: str, tight: bool = False) -> None:
        self.motor_controller.driving_direction = direction
        self.motor_controller.tight_corner = tight

    def on_button_click(self, _):
        """Start Sequence"""
        print("Button clicked!")
        self.drive_thread = Thread(target=self.motor_controller.drive, name="drive_thread")
        self.drive_thread.start()

    def start(self, listen=True):
        self.button.listen()
        if not listen:
            self.button.emulate_click()
