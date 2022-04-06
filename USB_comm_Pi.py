import serial
import time

ser = serial.Serial('/dev/ttyUSB0', 9600, timeout=5)

input_str = ser.readline()
print("Read input " + input_str.decode("utf-8").strip() + " from Arduino")

while 1:
    ser.write(b'status\n')
    input_str = ser.readline().decode("utf-8").strip()
    print("Read input back: " + input_str)

    time.sleep(2)

    ser.write(b'set on\n')
    input_str = ser.readline().decode("utf-8").strip()
    print("Read input back: " + input_str)

    time.sleep(2)

    ser.write(b'set off\n')
    input_str = ser.readline().decode("utf-8").strip()
    print("Read input back: " + input_str)

    time.sleep(2)