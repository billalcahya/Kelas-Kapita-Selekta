nama = "Billal Cahya"
nim = 672023165

a = 5

print (type(a))

x = 10.5
y = 5

print (x+y)

print(int(x)+y)

J = "PAGI"
H = "10.00"

print('{} {}'.format(H, J))

H = "Selamat Pagi"
H.upper()
H.lower()

H = H.upper()
print(H)

H = H.lower()
print(H)

print(H)

h = 'selamat pagi'

h_split_space = h.split(' ')
print(h_split_space)

print(h)

# String
a = 'Alfamart'
print(a)

# Integer
b = 5
print(b)
print(str(b))

print(type(b))   
print(type(str(b))) 

# Float
c = 10.5
print(c)
print(type(c))
print(int(c))

d = True
e = False

print(d)
print(e)

# Boolean
d = True
e = False

print(d)
print(type(d))
print(type(e))

f = "True"
print(f)
print(type(f))

print (a,b,c,d,e,f)

string1 = "Alfamart"
string2 = "Tangerang"
print (string1 + " " + string2)

angka1 = 10.5 
print(angka1)
print(int(angka1))
print(round(angka1))
print(type(round(angka1)))

angka2 = 7
print(7)
print(float(angka2))

string3 = "21"
print(int(string3))

# String Manipulation
kalimat1 = "Python itu mudah dan menyenangkan"
kalimat2 = "    Hello World    "
print(kalimat2.strip())
print(kalimat2.rstrip()) # Menghilangkan spasi
print(kalimat2.lstrip()) # Menghilangkan spasi

print(kalimat1)
print(kalimat1[0])
print(kalimat1[2])

print(kalimat1[:6])
print(kalimat1[-12:])

print(kalimat1.upper())
print(kalimat1.capitalize())
print(kalimat1.title())

print(kalimat1.replace("mudah", "seru"))

# String Formatting
nama = "Albi"
umur = 24
print("Halo nama saya", nama)

print(f"Halo nama saya {nama}")
print("Halo nama saya {}".format(nama))
print("Halo nama saya {1} Umur saya {0}".format(umur,nama))
print("Halo nama saya {n} Umur saya {u}".format( u = umur, n = nama))

# Input Output 
# nama = input("Nama kamu adalah : " )
# umur = input("Umur kamu adalah : " )

print(nama, umur)

# List
buah = ["anggur", "apel", "jeruk"]
print(buah[0])
print(buah[1])
print(buah[2])

buah.append("pisang")

# Dictionary
data = {
    "nama" : "Albi",
    "umur" : 24
}

print(data)
print(data["umur"])

data["alamat"] = "Tangerang"
print(data)

# Delete Variabel
string_awal = "Selamat Pagi"
# print(string_awal)

# del string_awal
print(string_awal)

# If Statement
jumlah_barang = 3

if jumlah_barang > 0 :
    print("Kamu punya barang")
    
suhu = 25

if suhu > 30 :
    print("Hari Panas")
    
#If Else Statement
baterai = 25
if baterai >= 20:
    print("Baterai Cukup")
else:
    print("Harus chas")
    
nilai_akhir = 75
kehadiran = 65

if nilai_akhir >= 70 and kehadiran>= 75:
    print("Lulus")
else : 
    print("Tidak Lulus")
    
# Nested Statement
presensi = 80
nilai_tugas = 70

if presensi >= 75:
    if nilai_tugas >= 60:
        print("Boleh ikut ujian")
    else :
        print("Nilai tugas kurang, gaboleh ikut ujian")
else :
    print("Presensi kurang. Tidak boleh ikut ujian")
    
nilai_akhir = 82
tugas_akhir = " tidak lengkap"
plagiarisme = False

if nilai_akhir >= 75:
    if tugas_akhir == "lengkap":
        if not plagiarisme:
            print("Lulus tanpa revisi")
        else:
            print("Tidak lulus karena plagiarisme")
    else :
        print("Lulus bersyarat")
else:
    print("Tidak lulus karena nilai rendah")
    
# For Loop
for i in range (1,6):
    print(i)

buah = ["apel", "pisang", "jeruk", "anggur"]

for item in buah:
    print(item)
    
# While Loop
angka = 3

while angka > 0:
    print(angka)
    angka -= 1
    
angka = 1
while angka <= 10:
    if angka % 2 == 0:
        print("Bilangan Genap", angka)
    angka += 1    
    
# Nested Loop
for i in range(1,4):
    for j in range(1,4):
        hasil = i * j
        print(f"{i} * {j} = {hasil}")
    print("---")

# Break
for angka in range (1,10):
    if angka == 5:
        break
    print("Angka : ", angka)
    
# Continue
for angka in range (1,6):
    if angka == 3:
        continue
    print("angka", angka)
    
# Pass
for i in range (1,5):
    if i == 3:
        pass
        print("pass")
    else:
        print("angka" , i)
        
# File Handling
with open("contoh.txt", "r") as file:
    isi = file.read()
    print(isi)
        
with open ("contoh.txt", "w") as file :
    file.write("aku belajar")

# with open ("contoh_baru.txt", "x") as file :
#     file.write("File baru dibuat")
    
with open("contoh.txt", "a") as file:
    file.write("\nusman belajar")

# Function tanpa parameter
def tampil():
    print("Selamat belajar python")
    
tampil()

def salam(nama):
    print("halo, ", nama)
    
salam("Billal")

# Function dengan return
def tambah(a,b):
    return a+b

hasil = tambah(5,3)
print(hasil)

# Function dengan kondisi
def cek_wahana(usia):
    if usia >= 12:
        print("Boleh naik wahana")
    else : 
        print("Tidak boleh naik wahana")
        
cek_wahana(10)

# Function dengan for
def sapa(nomer):
    print("halo ke - ", nomer)
    
for i in range (1,6):
    sapa(i)
    
import Kalkulator

hasil1 = Kalkulator.tambah(5,3)
hasil2 = Kalkulator.kurang(10,4)
hasil3 = Kalkulator.kali(3,4)
hasil4 = Kalkulator.bagi(10,2)

print("hasil1 : ", hasil1)
print("hasil2 : ", hasil2)
print("hasil3 : ", hasil3)
print("hasil4 : ", hasil4)

# Random modul bawan python angka acak

import random

angka = random.randint(1,10) # angka acak 1 sampai 10
print("angka acak : ", angka)

# Modul bawaan python datetime
import datetime

sekarang = datetime.datetime.now()
print("Waktu sekarang : ", sekarang)

# Try Except
try:
    angka = int(input("Masukkan angka : "))
    print("hasil : ", 10/angka)
except ZeroDivisionError :
    print("Tidak bisa dibagi dengan 0")
except ValueError :
    print("Input bukan angka")
    
# ============================================
# RANGKUMAN MATERI PYTHON HARI INI
# ============================================

# 1. Variabel dan Tipe Data
# - Menyimpan data: string, integer, float, boolean
# - Mengecek tipe data dengan type()
# - Konversi tipe data: int(), float(), str(), round()

# ============================================
# 2. Manipulasi String
# - upper(), lower(), capitalize(), title(), replace()
# - split() untuk memisahkan string menjadi list
# - strip(), lstrip(), rstrip() untuk menghapus spasi
# - Indexing dan slicing untuk mengambil bagian string

# ============================================
# 3. String Formatting
# - Menggabungkan variabel ke string dengan f-string atau .format()

# ============================================
# 4. List
# - Menyimpan banyak data dalam satu variabel
# - Menambahkan item menggunakan append()

# ============================================
# 5. Dictionary
# - Menyimpan data dengan pasangan key-value
# - Menambah, mengakses, mengubah value berdasarkan key

# ============================================
# 6. Percabangan (If, Else, Nested If)
# - If untuk kondisi
# - Else sebagai alternatif jika kondisi tidak terpenuhi
# - Nested if untuk kondisi di dalam kondisi lain
# - Operator logika: and, or, not

# ============================================
# 7. Looping
# - For loop: mengulang dengan range() atau list
# - While loop: mengulang selama kondisi True
# - Break: menghentikan loop
# - Continue: melewati iterasi tertentu
# - Pass: placeholder tanpa aksi

# ============================================
# 8. File Handling
# - Membaca file dengan mode 'r'
# - Menulis file dengan mode 'w' (overwrite)
# - Menambahkan isi file dengan mode 'a' (append)
# - Membuat file baru dengan mode 'x'

# ============================================
# 9. Function (Fungsi)
# - Fungsi tanpa parameter
# - Fungsi dengan parameter
# - Fungsi dengan return untuk mengembalikan nilai
# - Fungsi dapat memiliki kondisi dan loop di dalamnya

# ============================================
# 10. Modul
# - Menggunakan modul buatan sendiri (contoh: Kalkulator)
# - Menggunakan modul bawaan Python:
#   - random: menghasilkan angka acak
#   - datetime: mendapatkan waktu sekarang

# ============================================
# 11. Try-Except
# - Menangani error dengan try-except
# - ZeroDivisionError: pembagian dengan nol
# - ValueError: input bukan angka

# ============================================
# END OF RANGKUMAN
# ============================================
