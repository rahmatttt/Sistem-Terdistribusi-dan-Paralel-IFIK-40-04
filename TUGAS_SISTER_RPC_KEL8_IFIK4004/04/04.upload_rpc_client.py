# import xmlrpc bagian client
import xmlrpc.client

# buat stub proxy client
proxy = xmlrpc.client.ServerProxy("http://10.20.32.4:8001/")

# buka file yang akan diupload
with open("file_diupload.txt",'rb') as handle:
    # baca file dan ubah menjadi biner dengan xmlrpc.client.Binary
    binary_data = xmlrpc.client.Binary(handle.read())
proxy.file_upload(binary_data)

# panggil fungsi untuk upload yang ada di server
print(proxy.file_upload(binary_data))