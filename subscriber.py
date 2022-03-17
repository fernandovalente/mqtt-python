import time
import paho.mqtt.client as mqtt


def on_message(client, userdata, message):
    print("Message received: ", str(message.payload.decode("utf-8")))
    print("Message topic: ", message.topic)
    print("Message qos: ", message.qos)
    print("Message retain flag: ", message.retain)


mqtt_broker = "mqtt.eclipseprojects.io"
client = mqtt.Client("dashboard")
client.connect(mqtt_broker)

client.loop_start()
client.subscribe("/sensors/temperature")
client.on_message = on_message
time.sleep(30)
client.loop_end()
