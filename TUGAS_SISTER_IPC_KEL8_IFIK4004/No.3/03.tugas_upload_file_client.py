# import library socket karena menggunakan IPC socket
import socket

# definisikan IP server tujuan file akan diupload
host = "10.20.1.250"

# definisikan port number proses di server
port = 50007

# definisikan ukuran buffer untuk mengirim
bufer = 4096

# buat socket (apakah bertipe UDP atau TCP?) TCP
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)


# lakukan koneksi ke server
s.connect((host, port))


# buka file bernama "file_diupload.txt bertipe byte
f = open("file_diupload.txt","rb")
# masih hard code, file harus ada dalam folder yang sama dengan script python


try:
    # baca file tersebut sebesar buffer 
    byte = f.read(bufer)
    
    # selama tidak END OF FILE; pada pyhton EOF adalah b''
    while byte != b'':
        # kirim hasil pembacaan file
        print("sending...")
        s.send(byte)
        
        # baca sisa file hingga EOF
        byte = f.read(bufer)
        #print(byte)
        print(byte)
finally:
    print ("end sending")
    
    # tutup file jika semua file telah  dibaca
    f.close()

# tutup koneksi setelah file terkirim
s.close()