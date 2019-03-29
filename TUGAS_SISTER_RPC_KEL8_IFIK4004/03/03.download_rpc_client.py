# import xmlrpc bagian client
import xmlrpc.client


# buat proxy untuk mengakses server. Gunakan parameter URL server yang akan diakses berupa IP dan port. Bentuk http://IP:port
proxy = xmlrpc.client.ServerProxy("http://10.20.32.4:8001")

# buat/buka file baru dengan nama "hasil_download.txt" sebagai hasil download dari server
with open("hasil_download.txt","wb") as handle:
    handle.write(proxy.file_download().data)
    # tulis/isi file hasil_download.jpg dengan hasil dari memanggil fungsi "download" yang berada server
    # ubah file menjadi binary dengan menambahkan .data
    
    
