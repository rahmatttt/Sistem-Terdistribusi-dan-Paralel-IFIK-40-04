#program ini berfungsi untuk mendownload file image yang ada pada url

import os # memanggil library os (untuk melakukan perintah ping)
import requests # memanggil library request
import threading # memanggil library threading 
import urllib.request, urllib.error, urllib.parse #memanggil library urllib.request, urllib.error, urllib.parse  
import time #memanggil library time

url = "https://apod.nasa.gov/apod/image/1901/LOmbradellaTerraFinazzi.jpg" #memasukkan file (gambar) pada variabel url


def buildRange(value, numsplits):#fungsi buildrange dengan parameter value dan numsplits
    lst = [] #variabel lst yang menampung array list 
    for i in range(numsplits): #perulangan i sebanyak numsplits
        if i == 0: #kondisi saat i sama dengan 0
            lst.append('%s-%s' % (i, int(round(1 + i * value/(numsplits*1.0) + value/(numsplits*1.0)-1, 0)))) #nilai yang ditampung kedalam variabel lst berbentuk arraylist
        else: #kondisi selain i sama dengan 0
            lst.append('%s-%s' % (int(round(1 + i * value/(numsplits*1.0),0)), int(round(1 + i * value/(numsplits*1.0) + value/(numsplits*1.0)-1, 0)))) #nilai yang ditampung kedalam variabel lst berbentuk arraylist
    return lst #mengembalikan nilai yang ada divariabel lst

class SplitBufferThreads(threading.Thread): #membuat class splitbufferthreads dengan parameter from threading import thread
    """ Splits the buffer to ny number of threads
        thereby, concurrently downloading through
        ny number of threads.
    """
    def __init__(self, url, byteRange): #definisi constructor dengan parameter self, url, byteRange
        super(SplitBufferThreads, self).__init__() #memanggil class parent dalam constructor
        self.__url = url #melakukan set url
        self.__byteRange = byteRange #melakukan set batasan byte
        self.req = None #melakukan set required menjadi tidak ada (none)

    def run(self): #membuat fungsi run dengan parameter self
        self.req = urllib.request.Request(self.__url,  headers={'Range': 'bytes=%s' % self.__byteRange}) #melakukan set required pada url yang sudah dibuat dengan batasan header sebesar byteRange  

    def getFileData(self): #membuat fungsi getFileData dengan parameter self
        return urllib.request.urlopen(self.req).read() #mengembalikan nilai url yang telah dibaca


def main(url=None, splitBy=3): #fungsi main dengan parameter url=none, dan splitby=3
    start_time = time.time() #mengembalikan nilai waktu saat ini dalam detik (dihitung dari 1 Januari 1970 sampai waktu sekarang)
    if not url: #kondisi disaat not url
        print("Please Enter some url to begin download.") #menampilkan string disaat kondisi not url "please enter some url to begin donwload "
        return #mengembalikan nilai kosong

    fileName = url.split('/')[-1] #membagi url, dipisahkan dengan '/'
    sizeInBytes = requests.head(url, headers={'Accept-Encoding': 'identity'}).headers.get('content-length', None) #memasukkan bytes request header ke dalam sizeinbytes
    print("%s bytes to download." % sizeInBytes) #menampilkan sizeinbytes
    if not sizeInBytes:#kondisi saat not sizeinbytes
        print("Size cannot be determined.") #menampilkan string saat kondisi not sizeinbytes "size cannot be determined "
        return #mengembalikan nilai 

    dataLst = [] ##variabel dataLst yang menampung array list
    for idx in range(splitBy): #looping sebanyak splitBy
        byteRange = buildRange(int(sizeInBytes), splitBy)[idx] #memanggil fungsi buildRange
        bufTh = SplitBufferThreads(url, byteRange) #memanggil fungsi SplitBufferThreads
        bufTh.start() #memulai thread - start
        bufTh.join() #join thread ke server yang sudah didefinisikan
        dataLst.append(bufTh.getFileData()) #memasukkan data bufTh ke dalam list

    content = b''.join(dataLst) #membuat variabel content yang berisi fungsi join dataLst

    #percabangan
    if dataLst:
        if os.path.exists(fileName):
            os.remove(fileName) #menghapus fileName
        print("--- %s seconds ---" % str(time.time() - start_time))#menampilkan selisih antara waktu sekarang dan waktu awal
        with open(fileName, 'wb') as fh: #membuka file
            fh.write(content) #menulis teks didalam filename
        print("Finished Writing file %s" % fileName) #menampilkan filename 

if __name__ == '__main__': #eksekusi program
    main(url) #memanggil fungsi main dengan parameter url