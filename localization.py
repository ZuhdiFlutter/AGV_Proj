import multiprocessing
from RFID import *
from events import *

orientation = 1  #---------1-4.-----each turn will increase 1. This is to add to location using encoders
readRFID = multiprocessing.Process(target=RFIDloc)

#---------------below is the code snippets example for encoder-------------------
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