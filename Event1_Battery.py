import RPi.GPIO as GPIO  #Import GPIO library
import time

GPIO.setmode(GPIO.BCM)  # programming the GPIO by BCM pin numbers

BATTERY_PORT = 17  #-----------dummy port------------
LED_PORT = 10  #-----------dummy port------------

GPIO.setup(BATTERY_PORT, GPIO.IN)

#GPIO.setup(LED_PORT, GPIO.OUT)

#------------Lower than 1.2V is low voltage-------------
#-----------Make potential divider circuit R1:R2 is 9:1
#-----------Low voltage of Lipo is 3.6V/cell, low reading of Rpi is 1.19V
#GPIO.output(LED_PORT, 0)

battery_conf = 0


def BatteryCase():
    while True:  # this will carry on until you hit CTRL+C
        if GPIO.input(17):  # if port 17 == 1
            print("Port 17 is 1/HIGH/True")
            battery_conf = 0
        else:
            print("Port 17 is 0/LOW/False")
            battery_conf = battery_conf + 1
        time.sleep(0.2)  # wait 2 seconds
        if battery_conf == 10:
            print("BATTERY LOW!")
