import time
import paho.mqtt.client as mqtt
from random import randrange, uniform

mqtt_broker = "mqtt.eclipseprojects.io"
client = mqtt.Client("temperature_inside")
client.connect(mqtt_broker)

while True:
    rand_num = uniform(20, 21)
    client.publish("/sensors/temperature", rand_num)
    print(f'Published {rand_num} to topic /sensors/temperature')
    time.sleep(1)
