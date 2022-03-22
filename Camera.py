import cv2                  #import opencv
import apriltag             #import apriltag
import numpy                #import numpy needed for apriltag
import argparse             #import argparse needed for apriltag

cap = cv2.VideoCapture(0)   #open camera using default backend

img = cv2.imread('apriltag_foto.jpg'.cv2.IMREAD_GRAYSCALE)

detector = apriltag.Detector()
result = detector.detect(img)
