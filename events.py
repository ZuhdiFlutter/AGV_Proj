import multiprocessing
from Event2_sonar import *
from Event1_Battery import *

urgency_level = 0

readDist = multiprocessing.Process(target=ObstacleCase)
readBatt = multiprocessing.Process(target=BatteryCase)