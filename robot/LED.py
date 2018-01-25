from time import sleep

import RPi.GPIO as GPIO


class LED:
    def __init__(self, pin: int, blink_interval: int = 0.25):
        self.pin = pin
        self.led = GPIO.setup(pin, GPIO.OUT)
        self.is_on = False
        self.blink_interval = blink_interval

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.off()

    def on(self):
        """This turns on the LED"""
        self.is_on = True
        GPIO.output(self.pin, GPIO.HIGH)

    def off(self):
        """Take a guess what this does"""
        self.is_on = False
        GPIO.output(self.pin, GPIO.LOW)

    def toggle(self):
        """Toggles the LED on or off"""
        self.is_on = not self.is_on
        GPIO.output(self.pin, GPIO.HIGH if self.is_on else GPIO.LOW)

    def blink(self):
        """Blink the LEDs"""
        while True:
            self.toggle()
            sleep(self.blink_interval)

    def reset(self):
        """Resets the LED"""
        self.off()
