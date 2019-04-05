# import paho
import paho.mqtt.client as mqtt


# definsi broker yang digunakan
broker = "10.20.0.170"


# buat client bernama P1
print("creating new instance")
client = mqtt.Client("P1")


# client terkoneksi ke broker
print("connecting to broker")
client.connect(broker, port=3333)


# print "baca file"
print ("read file")
f = open("surf.jpg", "rb")
# buka file surf.jpg


# baca semua isi file
biner_gambar = f.read()


# ubah file dalam bentuk byte gunakan fungsi byte()

# publish dengan topik photo dan data dipublish adalah file
print("publish foto")
client.publish("photo",biner_gambar)

# client loop mulai
client.loop_start()


# tutup file
f.close()