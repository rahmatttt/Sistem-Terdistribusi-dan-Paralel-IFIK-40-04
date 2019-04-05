# import paho mqtt
import paho.mqtt.client as mqtt

# import time for sleep()
import time

# buat callback on_message; jika ada pesan
# maka fungsi ini akan dipanggil secara asynch
########################################
def on_message(client, userdata, message):
	print("Topic : ", message.topic)
	print("message received " ,str(message.payload.decode("utf-8")))

########################################
    
# buat definisi nama broker yang akan digunakan
broker_address="10.20.0.170"

# buat client baru bernama P1
print("creating new instance")
client = mqtt.Client("P1")

# kaitkan callback on_message ke client
client.on_message=on_message

# buat koneksi ke broker
print("connecting to broker")
client.connect(broker_address, port=3333)

# jalankan loop client
client.loop_start()

# client melakukan subsribe ke topik 1 dan topik 2
print("Subscribing to topic")
client.subscribe("topik 1")
client.subscribe("topik 2")

# loop forever
while True:
    # berikan waktu tunggu 1 detik 
	time.sleep(1)
    

#stop loop
client.loop_stop()