import paho.mqtt.publish as publish
 
MQTT_SERVER = "129.129.130.80"
MQTT_PATH = "test"
 
publish.single(MQTT_PATH, "blabla", hostname=MQTT_SERVER)
