# import os, re dan threading
import os
import re
from threading import Thread

# import time
import time

# buat kelas ip_check
class ip_check(Thread):
    
    # fungsi __init__; init untuk assign IP dan hasil respons = -1
    def __init__ (self,ip):
        Thread.__init__(self)
        self.ip = ip
        self.status = -1
    
    # fungsi utama yang diekseskusi ketika thread berjalan
    def run(self):
        # lakukan ping dengan perintah ping -n (gunakan os.popen())
        ping_out = os.popen("ping -n 2 "+ip,"r")
       
        
        # loop forever
        while True:
            # baca hasil respon setiap baris
            line = ping_out.readline()
            
            # break jika tidak ada line lagi
            if not line: break
            
            # baca hasil per line dan temukan pola Received = x
            igot = re.findall(ip_check.lifeline,line)
            
            # tampilkan hasilnya
            if igot:    
               self.status = int(igot[0])

                
    # fungsi untuk mengetahui status; 0 = tidak ada respon, 1 = hidup tapi ada loss, 2 = hidup
    def status(self):
        # 0 = tidak ada respon
        if self.status == 0:
            return "tidak ada respon"
            
        # 1 = ada loss
        elif self.status == 1:
            return "ada loss"

        # 2 = hidup
        elif self.status == 2:
            return "hidup"
        # -1 = seharusnya tidak terjadi
        elif self.status == -1:
            return "seharusnya tidak terjadi"

# buat regex untuk mengetahui isi dari r"Received = (\d)"
ip_check.lifeline= re.compile(r"Received = (\d)")
report =  ("Tidak ada respon","Ada loss","hidup", "seharusnya tidak terjadi")
# report = status()
# catat waktu awal
start = time.time()

# buat list untuk menampung hasil pengecekan
check_results = []

# lakukan ping untuk 20 host
for suffix in range(1,20):
    # tentukan IP host apa saja yang akan di ping
    ip = "192.168.1."+str(suffix)
    
    # panggil thread untuk setiap IP
    current = ip_check(ip)
    
    # masukkan setiap IP dalam list
    check_results.append(current)
    
    # jalankan thread
    current.start()

# untuk setiap IP yang ada di list
for el in check_results:
    el = check_results[0]
    check_results = check_results[1:]
    
    # tunggu hingga thread selesai
    el.join()
    
    # dapatkan hasilnya
    #check_results.append(el)
    print ("Status from ",el.ip,"is",report[el.status])

# catat waktu berakhir
end = time.time()

# tampilkan selisih waktu akhir dan awal
print((end-start))
