import serial 

ser = serial.Serial('COM7', 115200)

while True:
    line = ser.readline().decode('utf-8').rstrip()
    print(line)

ser.close()