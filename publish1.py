import time
import paho.mqtt.client as mqtt
from random import randrange, uniform

mqtt_broker = "mqtt.eclipseprojects.io"
client = mqtt.Client("Temperature_Inside")
client.connect(mqtt_broker)

while True:
    rand_num = uniform(20, 21)
    client.publish("Temperature", rand_num)
    print(f'Published {rand_num} to topic TEMPERATURE')
    time.sleep(1)
