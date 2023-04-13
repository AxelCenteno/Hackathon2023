import serial 
from azure.iot.device import IoTHubDeviceClient, Message

ser = serial.Serial('COM7', 115200)

while True:
    line = ser.readline().decode('utf-8').rstrip()
    print(line)

ser.close()

CONNECTION_STRING = "HostName=MemorIA-IotHub.azure-devices.net;DeviceId=Sensor-Gas;SharedAccessKey=kWVv1XGi4OoCOMU6q2Foc/q4eQcNrr9BvWVhpxnQBlM="

def send_alert(message):
    try:
        client = IoTHubDeviceClient.create_from_connection_string(CONNECTION_STRING)
        client.connect()
        message = Message(message)
        client.send_message(message)
        print("Message sent successfully")
        client.disconnect()
    except Exception as e:
        print("Error sending message: {}".format(str(e)))