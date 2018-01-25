from threading import Thread

import RPi.GPIO as GPIO
from flask import Flask, request

from robot.Log import log
from robot.Robot import Robot

# Create flask instance and create a reference to the log
# For some reason we can't read the log if we don't do this ¯\_(ツ)_/¯
app = Flask(__name__, static_url_path='')
log_ref = log


def on_destination_reached():
    """Called when the robot reaches it's destination"""
    global robot
    log.write("Destination reached!")
    robot.reset()


# Set GPIO Mode
GPIO.setmode(GPIO.BCM)
robot = Robot(on_destination_reached)


@app.route('/', methods=["GET"])
def index():
    return app.send_static_file('index.html')


@app.route('/log', methods=["GET"])
def log():
    """Send the logstring to the client"""
    global log_ref
    return log_ref.read()


@app.route('/start', methods=["POST"])
def start():
    """Get the destination from the request body and start the robot"""
    global robot
    destination = request.get_json(cache=False)["destination"]
    robot.set_destination_string(destination)
    robot_thread = Thread(target=robot.start_driving)
    robot_thread.start()
    return "OK"
