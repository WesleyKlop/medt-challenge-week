from threading import Thread

import RPi.GPIO as GPIO
from flask import Flask, request

from robot.Log import log
from robot.Robot import Robot

app = Flask(__name__, static_url_path='')
log_ref = log


def on_destination_reached():
    global robot
    log.write("Destination reached!")
    robot.reset()


GPIO.setmode(GPIO.BCM)
robot = Robot(on_destination_reached)


@app.route('/', methods=["GET"])
def index():
    return app.send_static_file('index.html')


@app.route('/log', methods=["GET"])
def log():
    global log_ref
    return log_ref.read()


@app.route('/start', methods=["POST"])
def start():
    global robot
    destination = request.get_json(cache=False)["destination"]
    robot.set_destination_string(destination)
    robot_thread = Thread(target=robot.start_driving)
    robot_thread.start()
    return "OK"
