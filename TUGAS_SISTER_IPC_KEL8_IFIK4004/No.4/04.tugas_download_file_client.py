# import library socket karena menggunakan IPC socket
import socket

# definisikan IP server tujuan file akan diupload
host = "10.20.1.250"

# definisikan port number proses di server
port = 50007

# definisikan ukuran buffer untuk mengirim
bufer = 4096

# buat socket (apakah bertipe UDP atau TCP?)
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# lakukan koneksi ke server
s.connect((host,port))


# buka file bernama "hasil_download.txt bertipe byte
# masih hard code, file harus ada dalam folder yang sama dengan script python
f = open("hasil_download.txt","wb")

# loop forever
while 1:
    # terima pesan dari client
    print("downloading...")
    data = s.recv(bufer)
    
    # tulis pesan yang diterima dari client ke file kita (result.txt)
    f.write(data)
    
    # berhenti jika sudah tidak ada pesan yang dikirim
    if not data: break
    
# tutup file_hasil_download.txt    
f.close()

#tutup socket
s.close()