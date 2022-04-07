from Event1_Battery import *
from Event2_sonar import *
from RFID_pyconv import *
from CameraQR import *
import multiprocessing
from localization import *
import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BOARD)  # programming the GPIO by BCM pin numbers


def startCheck():
    if checkBattery() == 1:  #condition for enough battery
        print('enough battery')
        if checkDistance(
        ) > 3:  #condition for enough space to move (no obstacle)
            print('can move forward')
            if checkCamera(cap, detector) == 1:  #condition for QR detected
                print(
                    'QR detected'
                )  #-----------Clement&Troy: Make the AGV go around the track------
            elif checkCamera == 0:
                print('QR not found')
        else:  #---------------------------condition for obstacle infront when starting------
            print('obstacle infront')
        # cornerCond = 0
        # for corner in atCorners:
        #     if location == atCorners:  #need to find how to round off
        #         cornerCond = 1
        # if cornerCond == 1:  #at corners, can move
        #     print('turn right ONLY')
        # else:  #obstacle detected!!
        #     print('Avoid obstacles!')  #avoid obstacle!!

    else:  #battery insufficient
        print('battery insufficient')
        print('stop & buzzer'
              )  #--------Clement&Troy: Send to UNO---------------------


if __name__ == '__main__':
    readRFID.start()

    readRFID.join()
