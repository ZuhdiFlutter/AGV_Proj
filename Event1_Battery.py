import RPi.GPIO as GPIO  #Import GPIO library
import time

GPIO.setmode(GPIO.BCM)  # programming the GPIO by BCM pin numbers

BATTERY_PORT = 17  #-----------dummy port------------

GPIO.setup(BATTERY_PORT, GPIO.IN)

battery_conf = 0


def BatteryCase():
    global battery_conf
    while True:  # this will carry on until you hit CTRL+C
        if GPIO.input(17):  # if port 17 == 1
            print("Port 17 is 1/HIGH/True")
            battery_conf = 0
        else:
            print("Port 17 is 0/LOW/False")
            battery_conf = battery_conf + 1
        time.sleep(0.05)  # wait 2 seconds
        if battery_conf == 20:
            print("BATTERY LOW!")
            battery_conf = 0
