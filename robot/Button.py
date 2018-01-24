from time import sleep

import RPi.GPIO as GPIO


class Button:
    def __init__(self, pin: int, callback: callable(int)):
        self.pin = pin
        self.callback = callback
        GPIO.setup(self.pin, GPIO.IN, pull_up_down=GPIO.PUD_UP)
        self.click_count = 0

    def __exit__(self):
        """Called when object gets garbage collected"""
        GPIO.remove_event_detect(self.pin)

    def on_click(self, _: int):
        self.click_count += 1

    def emulate_click(self):
        """Emulate a button click"""
        self.on_click(self.pin)

    def listen(self):
        """Start listening for button click events"""
        GPIO.add_event_detect(self.pin, GPIO.RISING, callback=self.on_click, bouncetime=200)
        sleep(5)
        self.callback(self.click_count)
        return self
