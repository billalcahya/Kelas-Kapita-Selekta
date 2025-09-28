# Pengertian Kondisi If Bahasa Python

a = 12
b = 10
 
if a > b:
  print('Variabel a lebih besar dari variabel b')
  
a = 12
b = 10
 
if a > b:
  print('Variabel a lebih besar dari variabel b')
  print('Sedang belajar bahasa Python di Duniailkom')
  
a = 12
b = 12
 
if a > b :
  print('Variabel a lebih besar dari variabel b')
if a < b :
  print('Variabel a lebih kecil dari variabel b')
if a == b :
  print('Variabel a sama dengan variabel b')
  
a = 7

if (a % 2) == 0:
  print('Variabel a berisi angka genap')
if (a % 2) != 0:
  print('Variabel a berisi angka ganjil')
  
# Pengertian Kondisi If Else Bahasa Python

a = 7
 
if (a % 2) == 0:
  print('Variabel a berisi angka genap')
else:
  print('Variabel a berisi angka ganjil')

nilai = 65
 
if nilai >= 75:
  print('Selamat, anda lulus')
else:
  print('Maaf, silahkan coba lagi tahun depan')

# Pengertian Kondisi If Else If Bahasa Python

nilai = 'D'
 
if nilai == 'A':
  print('Pertahankan')
elif nilai == 'B':
  print('Harus lebih baik lagi')
elif nilai == 'C':
  print('Perbanyak belajar')
elif nilai == 'D':
  print('Jangan keseringan main')
elif nilai == 'E':
  print('Kebanyakan bolos...')
else:
  print('Maaf, format nilai tidak sesuai')

nilai = 65
print('Nilai:',nilai)
 
if nilai >= 90:
  print('Pertahankan')
elif (nilai >= 80) and (nilai < 90):
  print('Harus lebih baik lagi')
elif (nilai >= 60) and (nilai < 80):
  print('Perbanyak belajar')
elif (nilai >= 40) and (nilai < 60):
  print('Jangan keseringan main')
elif nilai < 40:
  print('Kebanyakan bolos...')
else:
  print('Maaf, format nilai tidak sesuai')