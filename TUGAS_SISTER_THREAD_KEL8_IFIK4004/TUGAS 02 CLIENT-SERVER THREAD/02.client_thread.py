# import socket dan sys
import socket
import sys

# fungsi utama
def main():
    # buat socket bertipe TCP
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    
    # tentukan IP server target
    IP = '10.20.1.192'
    
    # tentukan port server
    PORT = 33000 

    # lakukan koneksi ke server
    try:
        s.connect((IP, PORT))
        print ("\nConnecting...")   
    except:
        # print error
        print("Koneksi error")
        # exit
        sys.exit()
    # tampilkan menu, enter quit to exit
    print("Masukkan 'quit' untuk keluar")
    message = input(" -> ")

    # selama pesan bukan "quit", lakukan loop forever
    while message != 'quit':
        # kirimkan pesan yang ditulis ke server
        s.sendall(message.encode())
        
        # menu (user interface)
        message = input(" -> ")

    # send "quit" ke server
    s.send(b'--quit--')

# panggil fungsi utama
if __name__ == "__main__":
    main()