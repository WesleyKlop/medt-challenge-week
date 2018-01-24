from time import sleep

import RPi.GPIO as GPIO


class LED:
    def __init__(self, pin: int, blink_interval: int = 0.25):
        self.pin = pin
        self.led = GPIO.setup(pin, GPIO.OUT)
        self.is_on = False
        self.blink_interval = blink_interval

    def on(self):
        self.is_on = True
        GPIO.output(self.pin, GPIO.HIGH)

    def off(self):
        self.is_on = False
        GPIO.output(self.pin, GPIO.LOW)

    def toggle(self):
        self.is_on = not self.is_on
        GPIO.output(self.pin, GPIO.HIGH if self.is_on else GPIO.LOW)

    def blink(self):
        while True:
            self.toggle()
            sleep(self.blink_interval)
