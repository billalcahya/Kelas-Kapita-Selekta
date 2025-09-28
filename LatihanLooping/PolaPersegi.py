print("## Program Python Persegi Bintang ##")
print("## ============================== ##\n")

panjang = int(input("Input besar persegi : "))

for i in range (panjang):
    for j in range (panjang):
        print (i, end=" ")
    print()

print("## Program Python Persegi Panjang Bintang ##")
print("## ====================================== ##")
print()

tinggi = int(input("Masukkan Tinggi Persegi Panjang : "))
panjang = int(input("Masukkan Panjang Persegi Panjang : "))

for i in range (tinggi):
    for j in range (panjang):
        print (i , end= " ")
    print()

print ("## Program Python Segitiga Bintang ##")
print ("## =============================== ##")
print()

tinggi = int(input("Masukkan Tinggi Segitiga : "))

for i in range (tinggi):
    for j in range (i+1):
        print(i  , end= " ")
    print()
    
print ("## Program Python Segitiga Bintang Terbalik ##")
print ("## ======================================== ##")
print()

tinggi = int(input("Masukkan Tinggi Segitiga : "))

for i in range (tinggi):
    for j in range (tinggi - i):
        print ( i , end=" ")
    print()

print ("## Program Python Piramida Bintang ##")    
print ("## =============================== ##")
print()

tinggi = int(input("Masukkan Tinggi Bintang : "))

for i in range (tinggi):    
    for j in range (tinggi - i):
        print(" ", end= "")
    for k in range (i+1):
        print(k, end=" ")
    print()

print ("## Progam Python Piramida Bintang Terbalik ##")
print ("## ======================================= ##")
print()

tinggi = int(input("Masukkan Tinggi Segitiga : "))

for i in range (tinggi):
    for j in range (i+1):
        print (" " , end="")
    for k in range (tinggi - i):
        print(i, end=" ")
    print()

print ("## Program Pyton Belah Ketupat ##")
print ("## =========================== ##")
print()

tinggi = int(input("Masukkan Lebar Belah Ketupat : "))

for i in range (tinggi):    
    for j in range (tinggi - i):
        print(" ", end= "")
    for k in range (i+1):
        print(k, end=" ")
    print()

for i in range (1,tinggi):
    for j in range (i+1):
        print (" " , end="")
    for k in range (tinggi - i):
        print(i, end=" ")
    print()

