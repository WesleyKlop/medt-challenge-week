import RPi.GPIO as GPIO


class Button:
    def __init__(self, pin, callback):
        self.pin = pin
        self.callback = callback
        GPIO.setup(self.pin, GPIO.IN, pull_up_down=GPIO.PUD_UP)

    def __exit__(self):
        GPIO.remove_event_detect(self.pin)

    def emulate_click(self):
        self.callback(self.pin)

    def listen(self):
        GPIO.add_event_detect(self.pin, GPIO.RISING, callback=self.callback, bouncetime=200)
        return self
