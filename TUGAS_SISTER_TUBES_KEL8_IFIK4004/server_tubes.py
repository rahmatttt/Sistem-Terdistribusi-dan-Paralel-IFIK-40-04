import cv2
import numpy as np
import matplotlib.pyplot as plt
from xmlrpc.server import SimpleXMLRPCServer
from xmlrpc.server import SimpleXMLRPCRequestHandler
import xmlrpc.client
import threading
import socket
import sys

#nerima dari client
# buat socket TCP
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# lakukan binding ke IP dan port
s.bind(("localhost", 8000))

# lakukan listen
s.listen(10)

#  siap menerima koneksi
conn, addr = s.accept()

f = open("upload.png", "wb")


# loop forever
while 1:
    # terima pesan dari client
    data = conn.recv(4096)
    
    # tulis pesan yang diterima dari client ke file kita (result.txt)
    f.write(data)
    
    # berhenti jika sudah tidak ada pesan yang dikirim
    if not data: break
    
# tutup file    
f.close()

#tutup socket
s.close()

# tutup koneksi
conn.close()

file = "upload.png"
# end nerima dari client
hasil = "hasil.png"

class RequestHandler(SimpleXMLRPCRequestHandler):
    rpc_paths = ('/RPC2')

with SimpleXMLRPCServer(('localhost', 8000)) as server:
	server.register_introspection_functions()
	lock = threading.Lock()
    
	def imageToGreyScale():
		lock.acquire()
		img = cv2.imread(file,0)
		cv2.imshow('image',img)
		cv2.waitKey(0)
		cv2.destroyAllWindows()
		cv2.imwrite(hasil,img)
		lock.release()
		return True
    
	server.register_function(imageToGreyScale)
	
	def imageContrast():
		lock.acquire()
		img = cv2.imread(file,1)
		cv2.imshow('image',img)
		cv2.waitKey(0)
		cv2.destroyAllWindows()
		cv2.imwrite(hasil,img)
		lock.release()
		return True
		
	server.register_function(imageContrast)
	
	def imageSmoothing():
		lock.acquire()
		img = cv2.imread(file)
		kernel = np.ones((5,5),np.float32)/25
		dst = cv2.filter2D(img,-1,kernel)
		plt.subplot(121),plt.imshow(img),plt.title('Original')
		plt.xticks([]), plt.yticks([])
		plt.subplot(122),plt.imshow(dst),plt.title('Averaging')
		plt.xticks([]), plt.yticks([])
		plt.savefig(hasil)
		plt.show()
		lock.release()
		return True
		
	server.register_function(imageSmoothing)
	
		
	
	print ("Server image processing berjalan...")
	
	server.serve_forever()

