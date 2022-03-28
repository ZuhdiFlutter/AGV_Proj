import multiprocessing
from RFID_pyconv import *

orientation = 1  #---------1-4
readRFID = multiprocessing.Process(target=readRFIDloc)
