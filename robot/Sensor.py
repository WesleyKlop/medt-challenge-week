import RPi.GPIO as GPIO


class Sensor:
    def __init__(self, pin, callback):
        self.pin = pin
        self.callback = callback
        GPIO.setup(self.pin, GPIO.IN)

    def __exit__(self):
        GPIO.remove_event_detect(self.pin)

    def emulate_sensor_change(self):
        """Acts as if a sensor changes"""
        self.callback(self.pin)

    def listen(self):
        """Start listening for changes in a sensor"""
        GPIO.add_event_detect(self.pin, GPIO.BOTH, callback=self.callback, bouncetime=200)
        return self

    def get_state(self):
        return GPIO.input(self.pin)

    def reset(self):
        GPIO.remove_event_detect(self.pin)
