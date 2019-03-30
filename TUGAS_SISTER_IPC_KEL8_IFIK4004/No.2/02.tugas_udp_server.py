# import library socket karena akan menggunakan IPC socket
import socket

# definisikan alamat IP bind dari server
HOST = '10.20.1.250'

# definisikan port number untuk bind dari server
PORT = 50007

# buat socket bertipe UDP
s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

# lakukan bind
s.bind((HOST, PORT))

# loop forever
while True:
    # terima pesan dari client
	data, addr = s.recvfrom(1024)
    # menampilkan hasil pesan dari client
	print("Pesan : ", data.decode())