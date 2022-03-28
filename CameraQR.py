#ref = https://core-electronics.com.au/tutorials/raspberry-pi/QR-codes-raspberry-pi.html#Soft

#from turtle import color
import cv2  #import opencv
import numpy as np

cap = cv2.VideoCapture(0)  #open camera using default backend
detector = cv2.QRCodeDetector()  #for QR

#---------------test using png file--------------------
# img = cv2.imread(r'C:\Users\Zuhdi\Downloads\testQR.png')


def checkCamera():
    global cap
    global detector
    while True:  #infinite loop to check at all times
        _, img = cap.read()  #get image of QR

        data, bbox, _ = detector.detectAndDecode(
            img)  #detecting QRdata, bounding box

        if (bbox is not None):
            # make the blue box around QR and display the data of QR
            for i in range(len(bbox)):
                cv2.line(
                    img,
                    tuple(bbox[i][0]),
                    tuple(bbox[(i + 1) % len(bbox)][0]),
                    color=(255, 0, 0),
                    thickness=2,
                )
            cv2.putText(img, data,
                        (int(bbox[0][0][0]), int(bbox[0][0][1]) - 10),
                        cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 250, 120), 2)

            if data:  #data can be read
                print('data found: ', data)
                # return 1
                #exec()
            #if data == 'Station1':
            #insert code to go to Station1
            #pass
            #if data == 'Parking1':
            #insert code to park at station1
            else:
                print('QR data not found!')
                # return 0
        cv2.waitKey(50)

        cv2.imshow("code detector", img)  #display live feedback camera

        if (cv2.waitKey(1) == ord("q")):
            break

    cv2.wait(10)
    cv2.VideoCapture(0).release()
    cv2.destroyAllWindows()


# checkCamera()
