from robot.Button import Button
from robot.Motor import Motor


class Robot:
    def __init__(self, pin_dict):
        self.left_motor = Motor(
            pin_dict["MOTOR_LEFT_PIN_1"],
            pin_dict["MOTOR_LEFT_PIN_2"],
            pin_dict["MOTOR_LEFT_PIN_3"],
            pin_dict["MOTOR_LEFT_PIN_4"])
        self.right_motor = Motor(
            pin_dict["MOTOR_RIGHT_PIN_1"],
            pin_dict["MOTOR_RIGHT_PIN_2"],
            pin_dict["MOTOR_RIGHT_PIN_3"],
            pin_dict["MOTOR_RIGHT_PIN_4"])
        self.button = Button(pin_dict["BUTTON"], self.on_button_click)

    def on_button_click(self, channel):
        """Start Sequence"""
