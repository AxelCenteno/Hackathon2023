from azure.iot.device import IoTHubDeviceClient, Message

CONNECTION_STRING = "HostName=MemorIA-IotHub.azure-devices.net;DeviceId=Camara;SharedAccessKey=iWEO9mHXrpUnK/jlQ2aFjOd1jJmzVY5GPAZMtRYtUQ8="

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

if __name__ == "__main__":
    send_alert("Alerta de ejemplo desde Python")