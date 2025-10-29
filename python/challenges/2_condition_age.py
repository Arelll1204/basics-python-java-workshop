# Program Klasifikasi Usia

# 1. TODO: Baca input dari pengguna
age = int(input("Masukkan umur anda: "))
# 2. TODO Tentukan kategori berdasarkan usia
if age < 0:
    kategori = "Usia tidak valid"
elif age < 13:
    kategori = "Anak-anak"
elif age < 18:
    kategori = "Remaja"
elif age < 60:
    kategori = "Dewasa" 
else:
    kategori = "Lansia"

print("Usia anda adalah", kategori)