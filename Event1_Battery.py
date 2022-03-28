#import RPi.GPIO as GPIO  #Import GPIO library

#GPIO.setmode(GPIO.BOARD)  # programming the GPIO by BCM pin numbers

BATTERY_PORT = 20  #-----------dummy port------------
LED_PORT = 10  #-----------dummy port------------

# GPIO.setup(BATTERY_PORT, GPIO.IN)

#GPIO.setup(LED_PORT, GPIO.OUT)

#------------Lower than 1.2V is low voltage-------------
#-----------Make potential divider circuit R1:R2 is 9:1
#-----------Low voltage of Lipo is 3.6V/cell, low reading of Rpi is 1.19V
#GPIO.output(LED_PORT, 0)


def checkBattery():
    if GPIO.input(BATTERY_PORT) == 1:
        GPIO.output(LED_PORT, 1)
        return 0
    else:
        GPIO.output(LED_PORT, 0)
        return 1