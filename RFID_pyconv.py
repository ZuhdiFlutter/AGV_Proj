from py532lib.i2c import *
from py532lib.frame import *
from py532lib.constants import *
import time
#https://www.youtube.com/watch?v=AUlefK47L0s&t=298s

location = [0, 0]
atCorners = [10, 0], [10, 10], [0, 10], [0, 10]


def setRFID():
    pn532 = Pn532_i2c()
    pn532.SAMconfigure()


card = Mifare()

while True:  #--------------------infinite loop for localization----------------------
    card_data = pn532.read_mifare().get_data()

    uid = card.scan_field()

    print(card_data)
    print(uid)

    uidtoCoord = {
        "uid1": [0, 0],
        "uid2": [1, 0],
        "uid3": [2, 0],
        "uid4": [3, 0],
        "uid5": [4, 0],
    }

    location = uidtoCoord[uid]

    print(location)

#---------------below is the code snippets for encoder-------------------
#time.sleep(.1)
# if (get encoder tick):
#     if orientation_state ==1:
#         location = [location[0]+0.2, location[1],]
#     elif orientation_state ==2:
#         location = [location[0], location[1]+0.2,]
#     elif orientation_state ==3:
#         location = [location[0]-0.2, location[1],]
#     elif orientation_state ==4:
#         location = [location[0], location[1]-0.2,]
#print(location)
#below is an example using another library------------------------------------
#http://shahrulnizam.com/arduino-lesson-mifare-reader-pn532/
#https://pypi.org/project/pn532pi/#description

# from pn532pi import Pn532I2c, Pn532

# i2c = Pn532I2c(1)
# nfc = Pn532(i2c)

# def setup():
#     nfc.begin()

#     versiondata = nfc.getFirmwareVersion()
#     if versiondata == null:
#         print("Didn't find PN53x board")
#         #while (1) # halt

#     # Got ok data, print it out!
#     print("Found chip PN5")

#     # configure board to read RFID tags
#     nfc.SAMConfig()

#     print("Waiting for an ISO14443A Card ...")

# while True:
#     success = nfc.readPassiveTargetID(PN532_MIFARE_ISO14443A, uid, uidlength)
#     if success:
#         print("card found")
#         print("uid value:" + uid)

#         uidtoCoord = {
#             "uid1": [0, 0],
#             "uid2": [1, 0],
#             "uid3": [2, 0],
#             "uid4": [3, 0],
#             "uid5": [4, 0],
#         }
#         location = uidtoCoord[uid]

#         print(location)