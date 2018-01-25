from time import sleep

from robot.LED import LED


class LEDOrchestrator:
    interval = 0.25

    def __init__(self, led_left_pin: int, led_right_pin: int):
        self.led_left = LED(led_left_pin)
        self.led_right = LED(led_right_pin)
        self.blink_on = False

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.both_off()

    def start_alternate_blink(self):
        """Alternate blinking between two lights"""
        self.blink_on = True
        while self.blink_on:
            if self.led_left.is_on:
                self.led_left.off()
                self.led_right.on()
            else:
                self.led_right.off()
                self.led_left.on()
            sleep(LEDOrchestrator.interval)

    def stop_blink(self):
        """Stops the blinken lights"""
        self.blink_on = False
        self.both_off()

    def both_on(self):
        """Turn both lights on"""
        self.led_left.on()
        self.led_right.on()

    def both_off(self):
        """:THINKING_FACE:"""
        self.led_right.off()
        self.led_left.off()

    def reset(self):
        """Reset the lights"""
        self.stop_blink()
