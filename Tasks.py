import RFID
import Communication
import time

def Avoid_Obstacle():
    buffer = RFID.Current_Location()
    time.sleep(0.5)
    Communication.WriteToUno('Stop')
    Communication.ReadFromUno() # Don't need if running in parallel
    time.sleep(0.25)
    Communication.WriteToUno('Avoid')
    Communication.ReadFromUno() # Don't need if running in parallel
    time.sleep(10)

def Go_To_Station(stop_coord):
    Communication.WriteToUno('Forward')
    Communication.ReadFromUno() # Don't need if running in parallel
    while 1:
        location = RFID.Current_Location()
        print("Location: ",location) # Don't need if running in parallel
        if location == stop_coord:
            time.sleep(0.5)
            Communication.WriteToUno('Stop')
            Communication.ReadFromUno() # Don't need if running in parallel
            return
        elif location == [0,0] or location == [0,7] or location == [5,7] or location == [5,0]:
            time.sleep(0.5)
            Communication.WriteToUno('Stop')
            Communication.ReadFromUno() # Don't need if running in parallel
            time.sleep(0.25)
            Communication.WriteToUno('Turn_Right')
            Communication.ReadFromUno() # Dont need if running in parallel
            time.sleep(2)
            Communication.WriteToUno('Forward')
            Communication.ReadFromUno() # Don't need if running in parallel

def Check_Station(station):
    if station == 'Station_1':
        print("Going to: ",station)
        Go_To_Station([0,4])
    elif station == 'Station_2':
        print("Going to: ",station)
        Go_To_Station([3,7])
    elif station == 'Station_3':
        print("Going to: ",station)
        Go_To_Station([5,3])
    else:
        print("Going to: ",station)
        Go_To_Station([2,0])