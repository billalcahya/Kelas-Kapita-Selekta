# Operasi Aritmatika

x = 20
y = 6
 
print('x + y =',x+y)
print('x - y =',x-y)
print('x * y =',x*y)
print('x / y =',x/y)
print('x // y =',x//y)
print('x % y =',x%y)
print('x ** y =',x**y)

# Operator Perbandingan Python

x = 7
y = 10
 
print('x =',x)
print('y =',y)
print('\n')
 
print('x == y hasilnya',x==y)
print('x != y hasilnya',x!=y)
print('x > y  hasilnya',x>y)
print('x < y  hasilnya',x<y)
print('x >= y hasilnya',x>=y)
print('x <= y hasilnya',x<=y)

a = 8
if (a % 2)==0:
  print('Variabel a berisi angka genap')
else:
  print('Variabel a berisi angka ganjil')
  
# Contoh Kode Program Operator Logika Python

print('Hasil dari True and True   :', True and True)
print('Hasil dari True and False  :', True and False)
print('Hasil dari False and True  :', False and True)
print('Hasil dari False and False :', False and False)
 
print('\n')
 
print('Hasil dari True or True   :', True or True)
print('Hasil dari True or False  :', True or False)
print('Hasil dari False or True  :', False or True)
print('Hasil dari False or False :', False or False)
 
print('\n')
 
print('Hasil dari not True  :', not True)
print('Hasil dari not False :', not False)

hasil = (5 > 6) and (10 <= 8)
print(hasil)
 
hasil = ('duniailkom' == 'duniailkom') or (10 <= 8)
print(hasil)
 
hasil = not (10 < 10)
print(hasil)
 
hasil = ('duniailkom' == 'duniailkom') and (10 <= 8) or (1 != 1)
print(hasil)

# Contoh Kode Program Operator Bitwise Python

x = 10
y = 12

 
print('x berisi angka',x ,'desimal atau',bin(x),'biner')
print('y berisi angka',y ,'desimal atau',bin(y),'biner')
 
print('\n')
 
print('x & y  :',x & y)
print('x | y  :',x | y)
print('x ^ y  :',x ^ y)
print('~x     :',~x)
print('x << 1 :',x << 1)
print('x >> 1 :',x >> 1)

# Contoh Kode Program Operator Assignment Python

a = 5
b = 3
b = b + 1
c = a + b
d = c + c + a
e = (c + d)* a
 
print('Isi variabel a:',a)
print('Isi variabel b:',b)
print('Isi variabel c:',c)
print('Isi variabel d:',d)
print('Isi variabel e:',e)

x = 10
x += 5
print('x += 5  :',x)
  
x = 10
x /= 5
print('x /= 5  :',x)
  
x = 10
x **= 5
print('x **= 5 :',x)
  
x = 10
x <<= 2
print('x <<= 2 :',x)

# Pengertian dan Contoh Operator Identitas Python
'''
is	Bernilai True jika kedua operand merujuk ke object yang sama dan berisi nilai yang sama
is not	Bernilai True jika kedua operand merujuk ke object yang tidak sama
'''

a = 5
b = 5
c = 6
print('a is b :', a is b)
print('a is c :', a is c)
print('a is not c :', a is not c)
print('\n')
  
i = 'Duniailkom'
j = 'Duniailkom'
print('i is j :', i is j)
print('i is not j :', i is not j)
print('\n');
  
x = ['a','b','c']
y = ['a','b','c']
print('x is y :', x is y)
print('x is not y :', x is not y)

x = ['a','b','c']
y = ['a','b','c']

print('x is y :', x is y)
print('x == y :', x == y)

print('id(x) :', id(x))
print('id(y) :', id(y))

'''
in	Bernilai True jika nilai yang dicari ada di dalam himpunan
not in	Bernilai True jika nilai yang dicari tidak ada dalam himpunan
'''

foo = 'Duniailkom'
print('foo :',foo)
print('\'i\' in foo     :', 'i' in foo)
print('\'k\' not in foo :', 'k' not in foo)
print('\'d\' not in foo :', 'd' not in foo)
print('\n')
 
 
bar = ['a','b','c']
print('bar :',bar)
print('\'a\' in bar     :', 'a' in bar)
print('\'a\' not in bar :', 'a' not in bar)
print('\'d\' not in bar :', 'd' not in bar)
print('\n')
 
baz = (12,43,102,55)
print('baz :',baz)
print('102 in baz     :', 102 in baz)
print('102 not in baz :', 102 not in baz)
print('35 not in baz  :', 35 in baz)
