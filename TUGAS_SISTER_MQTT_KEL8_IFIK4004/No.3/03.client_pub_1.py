# import paho mqtt
import paho.mqtt.client as mqtt


# import time untuk sleep()
import time


# import datetime untuk mendapatkan waktu dan tanggal
from datetime import datetime


# definisikan nama broker yang akan digunakan
broker = "10.20.0.170"


# buat client baru bernama P2
print("creating new instance")
client = mqtt.Client("P2")


# koneksi ke broker
print("connecting to broker")
client.connect(broker, port=3333)


# mulai loop client
client.loop_start()

# lakukan 20x publish topik 1
print("publish something")
for i in range (20):
    # sleep 1 detik
    time.sleep(1)
    # publish waktu sekarang topik 1
    client.publish("topik 1","AAA "+str(datetime.now()))

#stop loop
client.loop_stop()