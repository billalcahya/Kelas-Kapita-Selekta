# Pengertian Struktur Perulangan While Bahasa Python

i = 1
while i <= 5:
    print('Duniailkom')
    i += 1
    
i = 1
while i <= 5:
  print('Duniailkom', i)
  i += 1
  
i = 10
while i > 5:
  print('Duniailkom', i)
  i -= 1
  
i = 3
while i < 100:
  print(i)
  i = i + 3
  
warna = ['Merah','Biru','Kuning','Biru']
for i in warna:
  print(i)
  
warna = {'Merah','Biru','Kuning','Biru'}
for i in warna:
  print(i)
  
web = 'Duniailkom'
for huruf in web:
  print(huruf)
  
for i in range(5):
  print(i)
  
for i in range(5,10):
  print(i)
  
for i in range(3,100,3):
  print(i)
  
i = 1
while i <= 10:
  if i == 5:
    break
  print(i,' x ',i ,' = ',i*i)
  i += 1
  
for i in range(1,11):
  print(i,' x ',i ,' = ',i*i)
  if i == 5:
    break

for i in range(1,11):
  if i == 5:
    continue
  print(i,' x ',i ,' = ',i*i)
  
for i in range(1,11):
  print(i,' x ',i ,' = ',i*i)
  if i == 5:
    continue

i = 0
while i < 10:
  i += 1
  if i == 5:
    continue
  print(i,' x ',i ,' = ',i*i)
