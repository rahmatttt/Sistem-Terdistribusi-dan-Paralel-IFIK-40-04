# import library socket karena akan menggunakan IPC socket
import socket

# definisikan target IP server yang akan dituju
host="10.20.1.250"

# definisikan target port number server yang akan dituju
port = 50007

#print ("target IP:", UDP_IP)
print("target ip : ", host)
#print ("target port:", UDP_PORT)
print("target port : ", port)
#print ("pesan:", PESAN)
pesan = "udukudukudukuduk"
print("pesan : ", pesan)

# buat socket bertipe UDP
s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)


# lakukan loop 10 kali
for x in range (10):
    # definisikan pesan yang akan dikirim
    msg = pesan.encode()
    
    # kirim pesan
    s.sendto(msg, (host, port))
    
    