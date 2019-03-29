# import xmlrpc bagian client saja
import xmlrpc.client


# buat stub (proxy) untuk client
proxy = xmlrpc.client.ServerProxy("http://10.20.32.4:8000/RPC2")

# lakukan pemanggilan fungsi vote("nama_kandidat") yang ada di server
proxy.vote_candidate("Rahmat")
# lakukan pemanggilan fungsi querry() untuk mengetahui hasil persentase dari masing-masing kandidat
proxy.querry_result()

# lakukan pemanggilan fungsi lain terserah Anda