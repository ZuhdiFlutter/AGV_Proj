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

# import multiprocessing #import the multiprocessing library

# def parallel1(argument): #initialisation of function 1
#     Commands

# def parallel2(): #initialisation of function 2
#     Commands

# P1= multiprocessing.Process(target=parallel1, args=xyz)
# #target function1 to run using Process, pass in the argument

# P2= multiprocessing.Process(target=parallel2) # target function2 to run using Process

# if __name__ == '__main__': #necessary to run parallel in main function
#     P1.start() #start function1 separately
#     P2.start() #start function2 separately

#     P1.join() #blocks execution of main code until func1 complete
#     P2.join() #blocks execution of main code until func2 complete