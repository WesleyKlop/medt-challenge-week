import sys

import RPi.GPIO as GPIO

from robot.App import app

# Make the program easy to run
if __name__ == "__main__":
    try:
        GPIO.setmode(GPIO.BCM)
        GPIO.setwarnings(False)
        app.run(host='0.0.0.0', port=5000, debug=False)
    except KeyboardInterrupt:
        GPIO.cleanup()
        sys.exit(0)
