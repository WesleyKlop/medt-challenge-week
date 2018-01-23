from time import sleep

import RPi.GPIO as GPIO


class Motor:
    delay = 0.0025

    def __init__(self, pin1: int, pin2: int, pin3: int, pin4: int):
        self.pins = [pin1, pin2, pin3, pin4]
        GPIO.setup(self.pins, GPIO.OUT)

    def rotate(self, times: int = 1) -> None:
        """Sets all pins to GPIO.HIGH once for x times"""

        for i in range(times):
            for active_pin in range(0, 4):
                self.step(active_pin)
                sleep(self.delay)

    def step(self, pin_index: int) -> None:
        """Sets all pins to GPIO.LOW except for pin_index"""
        for pin in range(0, 4):
            # print("Setting pin{} to {}".format(self.pins[pin], GPIO.HIGH if pin == pin_index else GPIO.LOW))
            GPIO.output(self.pins[pin], GPIO.HIGH if pin == pin_index else GPIO.LOW)

    def step_backwards(self, pin_index: int) -> None:
        """Sets all pins to GPIO.LOW except for pin_index"""
        active_pin = 0
        if pin_index == 0:
            active_pin = 3
        elif pin_index == 1:
            active_pin = 2
        elif pin_index == 2:
            active_pin = 1
        elif pin_index == 3:
            active_pin = 0

        for pin in reversed(range(0, 4)):
            # print("Setting pin{} to {}".format(self.pins[pin], GPIO.HIGH if pin == pin_index else GPIO.LOW))
            GPIO.output(self.pins[pin], GPIO.HIGH if pin == active_pin else GPIO.LOW)
