import serial
import time

ser = serial.Serial('/dev/ttyUSB0', 9600, timeout=5)

# This function sends data to the Uno
def WriteToUno(data):
    temp = data + '\n'
    ser.write(temp.encode("utf-8"))

# This function reads data from the Uno serial monitor
def ReadFromUno():
    data = ser.readline().decode("utf-8").strip()
    print("From Uno: ",data)

if __name__ == '__main__':
    time.sleep(2)
    WriteToUno('Put_data_here')
    ReadFromUno()