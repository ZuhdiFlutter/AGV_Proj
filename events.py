import multiprocessing
from Event2_Sonar import *
from Event1_Battery import *
from Event3_QR import *

urgency_level = 0

readObst = multiprocessing.Process(target=ObstacleCase)
readBatt = multiprocessing.Process(target=BatteryCase)
readQR = multiprocessing.Process(target=QRCase)

# Detecting QR code,run in parallel
