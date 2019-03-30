# import library socket karena menggunakan IPC socket
import socket

# definisikan IP untuk binding
HOST = '10.20.1.250'

# definisikan port untuk binding
PORT = 50007

# definisikan ukuran buffer untuk menerima pesan
buffer = 4096

# buat socket (bertipe UDP atau TCP?)
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# lakukan binding ke IP dan port
s.bind((HOST, PORT))

# lakukan listen
s.listen(10)

#  siap menerima koneksi
conn, addr = s.accept()


# buka file bernama "file_didownload.txt
# masih hard code, file harus ada dalam folder yang sama dengan script python
f = open("file_didownload.txt", "rb")

try:
    # baca file tersebut sebesar buffer 
    byte = f.read(buffer)
    
	
    # selama tidak END OF FILE; pada pyhton EOF adalah b''
    while byte != b'':
        # kirim hasil pembacaan file dari server ke client
        conn.sendall(byte)
		
        # baca sisa file hingga EOF
        byte = f.read(buffer)
        
finally:
    print ("end sending")
    
    # tutup file jika semua file telah  dibaca
    f.close()

# tutup socket
s.close()

# tutup koneksi
conn.close()