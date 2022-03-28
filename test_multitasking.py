from threading import Thread
import multiprocessing
from CameraQR import *

import time


def measureTime(masa):
    while True:
        time.sleep(1)
        masa = masa + 1
        print(masa)


currentTime = 0
countT = Thread(target=measureTime, args=(currentTime))  #currentTime)
check1 = Thread(target=checkCamera,
                args=(
                    cv2.VideoCapture(0, cv2.CAP_DSHOW),
                    cv2.QRCodeDetector(),
                ))

try:
    while True:
        countT.start()
        check1.start()
        # check1.join()
        # countT.join()

except:
    print("Error: unable to start process")
