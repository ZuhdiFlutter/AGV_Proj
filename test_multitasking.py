import multiprocessing
from CameraQR import *
# from pynput.keyboard
import keyboard
import time

currentTime = 0


def measureTime():
    global currentTime
    while True:
        time.sleep(1)
        currentTime = currentTime + 1
        print(currentTime)
        if currentTime == 10:
            print('counting done')
            break


def inputP():
    while True:
        if keyboard.read_key() == "p":
            print("You pressed p")


countT = multiprocessing.Process(target=measureTime)  #currentTime)
check1 = multiprocessing.Process(target=checkCamera)
check2 = multiprocessing.Process(target=inputP)

if __name__ == '__main__':
    # freeze_support()
    countT.start()
    check1.start()
    check2.start()

    countT.join()
    check1.join()
    check2.join()
