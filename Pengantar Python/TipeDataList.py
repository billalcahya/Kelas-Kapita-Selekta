# Pengertian Tipe Data List Python

""" 

Secara sederhana, tipe data List adalah sebuah array,
yakni tipe data yang berisi kumpulan tipe data lain. 
Namun berbeda seperti array dalam bahasa pemrograman lain,
List bisa diisi dengan berbagai jenis data, tidak harus 
tipe data yang sama. Dan sebenarnya tipe data array di Python 
terdiri dari 4 jenis, yakni List, Tuple, Set dan Dictionary. 
Ke empat tipe data ini mirip satu sama lain dengan sedikit 
perbedaan. Kita akan bahas secara rinci dalam tutorial terpisah, 
yang dimulai dari List terlebih dahulu.

"""

foo = ["Belajar", "Python", "di", "Duniailkom"]
bar = [100, 200, 300, 400]
baz = ["Python", 200, 6.99, True]
  
print(foo)
print(bar)
print(baz)

# Cara Mengakses Tipe Data List Python

foo = ["Python", 200, 6.99, True, 'Duniailkom', 99j]
  
print(foo[0])
print(foo[1])
print(foo[2])
print(foo[3])
print(foo[4])
print(foo[5])

# Cara Mengganti Nilai Tipe Data List Python

foo = ["Python", 200, 6.99, True, 'Duniailkom', 99j]
print(foo)
  
foo[0] = 'Belajar'
foo[3] = False
print(foo)

# Menampilkan Sebagian Anggota List 

foo = ["Python", 200, 6.99, True, 'Duniailkom', 99j]
print(foo[2:5])
print(foo[:3])
print(foo[3:])
print(foo[:])