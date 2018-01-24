from threading import Thread

from robot.Button import Button
from robot.LED import LED
from robot.LEDOrchestrator import LEDOrchestrator
from robot.Motor import Motor
from robot.MotorController import MotorController
from robot.Pins import Pins
from robot.SensorController import SensorController


class Robot:

    def __init__(self):
        self.drive_thread = None  # type: Thread
        self.flashing_lights_thread = None  # type: Thread

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
            right_motor)

        self.sensor_controller = SensorController(
            Pins["SENSOR_LEFT"],
            Pins["SENSOR_MIDDLE"],
            Pins["SENSOR_RIGHT"],
            self.on_sensor_change)

        self.flashing_lights = LEDOrchestrator(Pins["LED_TOP_LEFT"], Pins["LED_TOP_RIGHT"])
        self.front_back_lights = LED(Pins["LED_FRONT_BACK"])
        self.front_back_lights.on()

        self.button = Button(Pins["BUTTON"], self.on_button_click)

    def on_sensor_change(self, direction: str, tight: bool = False) -> None:
        self.motor_controller.driving_direction = direction
        self.motor_controller.tight_corner = tight

    def on_button_click(self, click_count: int):
        """Start Sequence"""
        print("Button clicked! {} times".format(click_count))
        self.set_destination(click_count)
        self.drive_thread = Thread(target=self.motor_controller.drive)
        self.drive_thread.start()
        self.flashing_lights_thread = Thread(target=self.flashing_lights.start_alternate_blink)
        self.flashing_lights_thread.start()

    def set_destination(self, click_count: int):
        if click_count == 1:
            self.sensor_controller.destination = MotorController.DRIVING_DIRECTION_LEFT
        elif click_count == 2:
            self.sensor_controller.destination = MotorController.DRIVING_DIRECTION_STRAIGHT
        else:
            self.sensor_controller.destination = MotorController.DRIVING_DIRECTION_RIGHT

    def start(self, auto_start=False):
        self.button.listen()
        if auto_start:
            self.button.emulate_click()
