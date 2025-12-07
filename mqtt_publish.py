import paho.mqtt.client as mqtt
import json
import time

broker = "192.168.0.11"   
port = 1883
topic = "home/indu-2025/sensor"

username = "indusree0216"
password = "Indu*785"   

client = mqtt.Client()
client.username_pw_set(username, password)

client.connect(broker, port, 60)

while True:
    data = {
        "student_name": "Indu Sree",
        "temperature": 25,
        "humidity": 60,
        "vibration": 1,
        "unique_id": "42130187"
    }

    payload = json.dumps(data)
    result = client.publish(topic, payload)

    if result[0] == 0:
        print("Published:", payload)
    else:
        print("Failed to publish")

    time.sleep(5)
