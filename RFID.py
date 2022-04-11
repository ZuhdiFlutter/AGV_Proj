from py532lib.i2c import *
from py532lib.frame import *
from py532lib.constants import *
import time

prev_location = 0
temp_var = 0
location = ""


# This function will return the current location of the AGV
def Current_Location():
    uidToCoord = {
        "bytearray(b'K\\x01\\x01\\x00\\x04\\x08\\x04,\\x07\\xee\\x02')":
        [0, 0],
        "bytearray(b'K\\x01\\x01\\x00\\x04\\x08\\x04\\xdc\\xf3\\x99/')":
        [0, 1],
        "bytearray(b'K\\x01\\x01\\x00\\x04\\x08\\x04\\x9c\\xe1\\xda\"')":
        [0, 2],
        "bytearray(b'K\\x01\\x01\\x00\\x04\\x08\\x04\\xaa\\x80Px')": [0, 3],
        "bytearray(b'K\\x01\\x01\\x00\\x04\\x08\\x04\\xec8n\"')": [0, 4],
        "bytearray(b'K\\x01\\x01\\x00\\x04\\x08\\x04\\xec\\x8f\\xd3\"')":
        [0, 5],
        "bytearray(b'K\\x01\\x01\\x00\\x04\\x08\\x04<\\x82n\"')": [0, 6],
        "bytearray(b'K\\x01\\x01\\x00\\x04\\x08\\x04J\\xdcFx')": [0, 7],
        "bytearray(b'K\\x01\\x01\\x00\\x04\\x08\\x04\\x8c\\xcd\\xc0!')":
        [1, 7],
        "bytearray(b'K\\x01\\x01\\x00\\x04\\x08\\x04|\\x80n\"')": [2, 7],
        "bytearray(b'K\\x01\\x01\\x00\\x04\\x08\\x04Z5Cw')": [3, 7],
        "bytearray(b'K\\x01\\x01\\x00\\x04\\x08\\x04<\\x08l\"')": [4, 7],
        "bytearray(b'K\\x01\\x01\\x00\\x04\\x08\\x04<\\xb3\\xdb\"')": [5, 7],
        "bytearray(b'K\\x01\\x01\\x00\\x04\\x08\\x04\\x8c\\xf8i\"')": [5, 6],
        "bytearray(b'K\\x01\\x01\\x00\\x04\\x08\\x04<\\x9a\\xd6\"')": [5, 5],
        "bytearray(b'K\\x01\\x01\\x00\\x04\\x08\\x04\\xfc)u\"')": [5, 4],
        "bytearray(b'K\\x01\\x01\\x00\\x04\\x08\\x04\\x8cGn\"')": [5, 3],
        "bytearray(b'K\\x01\\x01\\x00\\x04\\x08\\x04L\\xe1\\xd4\"')": [5, 2],
        "bytearray(b'K\\x01\\x01\\x00\\x04\\x08\\x04<\\xa4p\"')": [5, 1],
        "bytearray(b'K\\x01\\x01\\x00\\x04\\x08\\x04\\xacD\\xb7!')": [5, 0],
        "bytearray(b'K\\x01\\x01\\x00\\x04\\x08\\x04\\xfcA\\xd3\"')": [4, 0],
        "bytearray(b'K\\x01\\x01\\x00\\x04\\x08\\x04\\x0c5\\xd3\"')": [3, 0],
        "bytearray(b'K\\x01\\x01\\x00\\x04\\x08\\x04\\\\3\\xdb\"')": [2, 0],
        "bytearray(b'K\\x01\\x01\\x00\\x04\\x08\\x04\\x1aoQx')": [1, 0],
        "bytearray(b'K\\x01\\x01\\x00\\x02\\x18\\x04\\x0f\\xde\\x81\\xf7')":
        [100, 100],
        "bytearray(b'K\\x01\\x01\\x00\\x02\\x18\\x04ol\\x06\\xf7')":
        [200, 200],
    }

    pn532 = Pn532_i2c()
    pn532.SAMconfigure()

    uid = str(pn532.read_mifare().get_data())
    location = uidToCoord[uid]
    print(location)
    return location


def RFIDloc():
    while True:
        location = Current_Location()
        print("Location: ", location)
        time.sleep(0.25)
