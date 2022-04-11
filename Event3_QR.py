import cv2  # Import OpenCV
import Tasks

qr_data = ""


# This function will return the QR code data
def QR():
    camera = cv2.VideoCapture(
        0)  # Set up a camera object which will be used to find OpenCV
    qr_detector = cv2.QRCodeDetector()  # QR code detection method

    while True:

        _, image = camera.read()  # Get the image of the QR code

        qr_data, qr_box, _ = qr_detector.detectAndDecode(
            image
        )  # Detect the bounding box coordinates and decode the QR data

        if (qr_box is not None):  # QR code bounding box is present
            if qr_data:  # QR code data is present
                return qr_data  # Return the data

        cv2.imshow(
            "QR Code Detector", image
        )  # Display the live camera feed to the desktop on Raspberry Pi OS preview

        if (cv2.waitKey(1) == ord("q")
            ):  # Press 'q' on the keyboard to stop the code
            break

    camera.release()  # Close the QR detector window once the code is stopped
    cv2.destroyAllWindows()


def QRCase():
    while True:
        qr_data = QR()
        if qr_data == 'Station_1' or qr_data == 'Station_2' or qr_data == 'Station_3' or qr_data == 'Station_4':
            # Start sensing for obstacles, run in parallel (can run in the Tasks module)
            # if (got obstacle):
            # Tasks.Avoid_Obstacle()
            # Tasks.Check_Station(qr_data)
            # print("At: ",qr_data)
            # continue
            print("QR data is: ", qr_data)
            Tasks.Check_Station(qr_data)
            print("At: ", qr_data)
