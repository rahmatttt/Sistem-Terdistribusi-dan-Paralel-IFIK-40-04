# import library socket karena akan menggunakan IPC socket
import socket

# definisikan tujuan IP server
host = "10.20.1.250"


# definisikan port dari server yang akan terhubung
port = 50007

# definisikan ukuran buffer untuk mengirimkan pesan
bufer = 4096

# definisikan pesan yang akan disampaikan
pesan = "halo"+host

# buat socket TCP
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)


# lakukan koneksi ke server dengan parameter IP dan Port yang telah didefinisikan
s.connect((host, port))

# kirim pesan ke server
s.sendall(pesan.encode())

# terima pesan dari server
data = s.recv(bufer)

# tampilkan pesan/reply dari server
print('Received ', data)

# tutup koneksi
s.close()

