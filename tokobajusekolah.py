print(20* "=")
print("TOKO BAJU SEKOLAH")
print(20* "=")
print("ADMIN")
print(20* "=")
print("\n")

A = input("Masukkan Username Anda :")
B = input("Masukkan Pasword Anda :")
username = ("INDAHDWI")
password = ("INDAH000")

if (A == username):   
    print("Login Anda Berhasil")
elif(B == password):
    print("Login Anda Berhasil")
else :
    print("Login Gagal")
print("\n")

#               0                    1               2                3  
#              -4                   -3              -2               -1     
baju = ["baju merah putih", "baju batik", "baju olahraga", "baju pramuka"]
harga = ["75.000","65.000","70.000","80.000"]
print(baju)
print(harga)

baju.append("baju lapangan")
harga.append("45.000")
print(baju)
print(harga)
print("\n")
baju.insert(2, "baju drumband")
harga.insert(2, "90.000")
print(baju)
print(harga)
print("\n")

print(baju[1], baju[3])
print(harga[1], harga[3])
print("\n")

baju[0] = "baju PDH"
harga[0] = "150.000"
print(baju)
print(harga)
print("\n")

baju.remove("baju drumband")
harga.remove("90.000")
baju.remove("baju PDH")
harga.remove("150.000")
baju.remove("baju lapangan")
harga.remove("45.000")
print(baju)
print(harga)

from prettytable import PrettyTable
table = PrettyTable()
table.field_names = ["No", "Jenis Baju sekolah", "harga"]
table.add_row([1, "baju merah putih", "75.000"])
table.add_row([2, "baju batik", "65.000"])
table.add_row([3, "baju olahraga", "70.000"])
table.add_row([4, "baju pramuka", "80.000"])
print(table)
print("\n")

print(20* "=")
print("PEMBELI")
print(20* "=")

a = 75.000
b = 65.000
c = 70.000
d = 80.000

beli = input("saya ingin membeli baju : ")

if beli == 'a' :
    print("anda membeli baju merah putih")

beli = input("saya ingin membeli baju : ")
if beli == 'b' :
    print("anda membeli baju batik")

beli = input("saya ingin membeli baju : ")
if beli == 'c' :
    print("anda membeli baju olahraga")

beli = input("saya ingin membeli baju : ")
if beli == 'd' :
    print("anda membeli baju pramuka")

else:
    print("stok habis")
print("\n")

print(20* "=")
print("NOTA BELANJA")
print(20* "=")

from prettytable import PrettyTable
table = PrettyTable()
table.field_names = ["banyak barang", "Jenis Baju sekolah", "harga"]
table.add_row([1, "baju merah putih", "75.000"])
table.add_row([1, "baju batik", "65.000"])
table.add_row([1, "baju olahraga", "70.000"])
table.add_row([1, "baju pramuka", "80.000"])
print(table)

from prettytable import PrettyTable
table = PrettyTable()
table.field_names = ["banyak barang", "jenis baju sekolah", "total"]
table.add_row([4, "semua baju sekolah", "290.000"])
print(table)
print("\n")