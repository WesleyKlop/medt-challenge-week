import RPi.GPIO as GPIO


class Button:
    def __init__(self, pin: int, callback: callable(int)):
        self.pin = pin
        self.callback = callback
        GPIO.setup(self.pin, GPIO.IN, pull_up_down=GPIO.PUD_UP)

    def __exit__(self):
        """Called when object gets garbage collected"""
        GPIO.remove_event_detect(self.pin)

    def emulate_click(self):
        """Emulate a button click"""
        self.callback(self.pin)

    def listen(self):
        """Start listening for button click events"""
        GPIO.add_event_detect(self.pin, GPIO.RISING, callback=self.callback, bouncetime=200)
        return self
