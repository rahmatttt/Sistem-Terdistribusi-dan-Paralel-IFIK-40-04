# gunakan library paho
import paho.mqtt.client as mqtt

# gunakan library time
import time

# buat callback pada saat ada pesan masuk
###########################################
def on_message(client, userdata, message):
    # tulis hasil file yang didapat bernama "iris.jpg"
	file = open("iris.jpg", "wb")
	file.write(message.payload)
	file.close()
##########################################
        
# definisikan broker yang akan digunakan
broker_address="10.20.0.170"

# buat client P2 
print("creating new instance")
client = mqtt.Client("P2")

# koneksi P2 ke broker
print("connecting to broker")
client.connect(broker_address, port=3333)

# P2 subcribe ke topik "photo"
print("Subscribing to topic","photo")
client.subscribe("photo")

# callback diaktifkan
client.on_message=on_message

#client.loop_forever()
while True:
    client.loop(15)
    time.sleep(2)