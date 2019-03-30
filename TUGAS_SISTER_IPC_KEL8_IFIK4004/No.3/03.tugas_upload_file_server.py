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

print ('Connection address:', addr)

# buka/buat file bernama hasil_upload.txt untuk menyimpan hasil dari file yang dikirim server
# masih hardcoded nama file, bertipe byte
f = open("hasil_upload.txt", "wb")


# loop forever
while 1:
    # terima pesan dari client
    data = conn.recv(buffer)
    
    # tulis pesan yang diterima dari client ke file kita (result.txt)
    f.write(data)
    
    # berhenti jika sudah tidak ada pesan yang dikirim
    if not data: break
    
# tutup file result.txt    
f.close()

#tutup socket
s.close()

# tutup koneksi
conn.close()
