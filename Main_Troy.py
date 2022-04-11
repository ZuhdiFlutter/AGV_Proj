import RFID
import Event3_QR
import Communication
import Tasks
import time

qr_data = ""
location = ""

# Sense for battery level, run in parallel

# Localisation, run in parallel (Might not need to)
while 1:
    location = RFID.Current_Location()
    print("Location: ", location)
    time.sleep(0.25)

# Detecting QR code,run in parallel

while 1:
    qr_data = Event3_QR.QR()
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

# Print output from serial monitor, run in parallel
# while 1:
# Communication.ReadFromUno()
