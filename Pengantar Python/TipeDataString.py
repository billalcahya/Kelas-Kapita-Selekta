#Tipe Data String
foo = "Belajar Python di Duniailkom"
print(foo)
 
#Tipe Data Integer
foo = 1500
print(foo)
 
#Tipe Data Float
foo = 99.123
print(foo)
 
#Tipe Data Complex Number
foo = 4j
print(foo)
 
#Tipe Data Boolean
foo = True
print(foo)
 
#Tipe Data List
foo = ["satu","dua","tiga","satu"]
print(foo)
 
#Tipe Data Tuple
foo = ("satu","dua","tiga","satu")
print(foo)
 
#Tipe Data Set
foo = {"satu","dua","tiga","empat"}
print(foo)
 
#Tipe Data Dictionary
foo = {"satu":1, "dua":2.13, "tiga":"a", "empat": True}
print(foo)

"""
Cara Pembuatan Tipe Data String Python
Di dalam bahasa Python, terdapat 3 cara untuk membuat tipe data string:

Menggunakan tanda kutip satu ( ' )
Menggunakan tanda kutip dua ( " )
Menggunakan tanda kutip satu atau dua sebanyak 3 kali ( ' ' ' ) atau (" " ")
"""

foo = "Duniailkom"
print(foo)
bar = 'Duniailkom'
print(bar)

foo = "Teks ini akan dipecah\nke dalam 2 baris"
print(foo)
foo = 'Teks ini\nakan dipecah\nke dalam 3 baris'
print(foo)

foo = '''Teks ini
akan dipecah
ke dalam 3 baris'''
print(foo)

# Operasi Penyambungan String (string concatenation)
foo = 'Belajar '
bar = "Bahasa Pemrograman Python "
baz = "di Duniailkom"
hasil = foo + bar + baz
print(hasil)

# String Python sebagai Array
foo = 'Duniailkom'
print(foo[0])
print(foo[4])
print(foo[5:10])

