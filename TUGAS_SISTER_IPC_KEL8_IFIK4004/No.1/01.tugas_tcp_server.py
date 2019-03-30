# import library socket karena akan menggunakan IPC socket
import socket

# definisikan alamat IP binding  yang akan digunakan 
HOST = '10.20.1.250'

# definisikan port number binding  yang akan digunakan 
PORT = 50007

# definisikan ukuran buffer untuk mengirimkan pesan
buffer = 4096

# buat socket bertipe TCP
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# lakukan bind
s.bind((HOST, PORT))

# server akan listen menunggu hingga ada koneksi dari client
s.listen(10)

# lakukan loop forever
while 1:
	# menerima koneksi
    conn, addr = s.accept()
	
	# menampilkan koneksi berupa IP dan port client yang terhubung menggunakan print
    print(conn)
	
	# menerima data berdasarkan ukuran buffer
    data = conn.recv(buffer)
	
	# menampilkan pesan yang diterima oleh server menggunakan print
    print("pesan = ", data.decode())
	
	# mengirim kembali data yang diterima dari client kepada client
    conn.sendall(data)

# tutup koneksi	
conn.close()

