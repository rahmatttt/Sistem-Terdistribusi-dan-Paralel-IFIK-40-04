import xmlrpc.client
import socket
import sys

# buat socket TCP
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# lakukan koneksi ke server
s.connect(('localhost', 8000))

# buka file bernama "tes.jpg" bertipe byte
f = open("tes.jpg","rb")

try:
    # baca file tersebut sebesar buffer 
    byte = f.read()
    
    # selama tidak END OF FILE; pada pyhton EOF adalah b''
    while byte:
        # kirim hasil pembacaan file
        print("sending...")
        s.send(byte)
        
        # baca sisa file hingga EOF
        byte = f.read()
finally:
    print ("end sending")
    
    # tutup file jika semua file telah  dibaca
    f.close()

# tutup koneksi setelah file terkirim
s.close()
proxy = xmlrpc.client.ServerProxy("http://localhost:8000/RPC2")
proxy.imageSmoothing()
