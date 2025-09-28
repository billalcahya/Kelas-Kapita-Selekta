# Pengertian Tipe Data Set Python

# Nilai data set tidak bisa menerima nilai ganda jika
# memiliki nilai ganda maka yang tersimpan hanya satu

foo = {"Belajar", "Python", "di", "Duniailkom"}
bar = {100, 200, 300, 400}
baz = {"Python", 200, 6.99, True}
 
print(foo)
print(bar)
print(baz)

foo = ["Belajar", "Python", "di", "Duniailkom"]
print(type(foo))
 
foo = ("Belajar", "Python", "di", "Duniailkom")
print(type(foo))
 
# Sifat Tipe Data Set Python
 
foo = {"Belajar", "Python", "di", "Duniailkom"}
print(type(foo))

foo = {"Belajar", "Python", "di", "Duniailkom", "di"}
bar = {100, 200, 300, 400, 200, 300}
 
print(foo)
print(bar)

# Operasi Himpunan tipe data Set Python

# Operasi gabungan (union), operasi irisan (intersection), 

foo = {1, 2, 3, 4, 5}
bar = {3, 4, 5, 6, 7}
 
print (foo | bar) # union
print (foo & bar) # intersection