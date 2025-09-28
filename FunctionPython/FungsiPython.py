# Cara Membuat Fungsi dalam Bahasa Python

def nama_function():
  # Isi function disini...
  # Isi function disini...
  return nilai

nilai = 10
print (nama_function())

def sapa_duniailkom():
  print("Halo Duniailkom")
 
sapa_duniailkom()
sapa_duniailkom()
sapa_duniailkom()

def sapa_lisa():
  print("Hai Lisa");
 
def sapa_sari():
  print("Morning, Sari");
 
def sapa_rudi():
  print("Halo bro,..");
 
sapa_lisa()
sapa_sari()
sapa_rudi()

def hitung_luas_segitiga():
  alas = 5
  tinggi = 7
  luas = (alas * tinggi) / 2
  print("Luas segitiga adalah: ",luas)
   
hitung_luas_segitiga()

# Pengertian Parameter dan Argumen Fungsi Python

def sapa_teman(nama):
  print("Hai",nama);
 
sapa_teman("Lisa")

def sapa_teman(nama):
  print("Hai",nama);
 
sapa_teman("Lisa")
sapa_teman("Sari")
sapa_teman("Putri")

def sapa_teman(nama1, nama2, nama3):
  print("Hai", nama1, nama2, nama3);
 
sapa_teman("Lisa", "Nova", "Putri")

def hitung_luas_segitiga(alas, tinggi):
  luas = (alas * tinggi) / 2
  print("Luas segitiga adalah: ",luas)
    
hitung_luas_segitiga(5, 7)
hitung_luas_segitiga(2, 10)
hitung_luas_segitiga(191, 357)

# Pengertian Perintah Return di dalam Function

def hitung_luas_segitiga(alas, tinggi):
  luas = (alas * tinggi) / 2
  return luas
    
var1 = hitung_luas_segitiga(5, 7)
print("Luas segitiga adalah:",var1)

# Perintah Return Akan Menghentikan Function Mirip Seperti Break

def harga_setelah_pajak(harga_dasar):
  return harga_dasar + (harga_dasar * 10/100)
 
harga_cilok = 5000
harga_final_cilok = harga_setelah_pajak(harga_cilok)
print("Harga cilok 1 porsi Rp.", harga_final_cilok)

def harga_setelah_pajak(harga_dasar):
  return harga_dasar + (harga_dasar * 10/100)
 
harga_cilok = 5000
harga_final_cilok = harga_setelah_pajak(harga_cilok)
print("Harga cilok 1 porsi Rp.", harga_final_cilok)

# Pengertian Default Parameter dalam Python

def tambah(var1 = 5, var2 = 2):
  return var1 + var2
 
print( tambah() )
print( tambah(1) )
print( tambah(1,2) )
print( tambah(5,4) )

def pangkat(angka, pangkat = 2):
  hasil = 1
  for i in range(0,pangkat):
    hasil = hasil * angka
  return hasil;
 
print( pangkat(3) )    
print( pangkat(5) )     
print( pangkat(10) )     
print( pangkat(3,3) )    
print( pangkat(5,4) )   
print( pangkat(6,6) )   

# Pengertian Named Parameter / Keyword Arguments

def pangkat(angka, pangkat = 2):
  hasil = 1
  for i in range(0,pangkat):
    hasil = hasil * angka
  return hasil;
 
print( pangkat(angka = 4,pangkat = 3) )      
print( pangkat(pangkat = 2,angka = 9) )      

def akses_database(address,username,password):
  print("====Database Connection====");
  print("server: ",address);
  print("username: ",username);
  print("password: ",password);
  print(".....connection success!");
   
akses_database("localhost","root","123456")

def akses_database(address,username,password):
  print("====Database Connection====");
  print("server: ",address);
  print("username: ",username);
  print("password: ",password);
  print(".....connection success!");
   
akses_database(username="admin",password="qwerty",address="192.168.0.4")

# Pengertian Arbitrary Arguments (*args) Python

def sapa_teman(*args):
  print(args)
  print(type(args))
   
sapa_teman("Alex","Nisa","Sari","Risa")

def sapa_teman(*nama):
  for i in nama:
    print("Halo",i)
   
sapa_teman("Alex","Nisa","Sari","Risa","Siska","Rudi","Joko")

def jumlah(*args):
  hasil = 0
  for i in args:
    hasil += i
  return hasil
   
print( jumlah(5,7) )
print( jumlah(5,7,3,2) )
print( jumlah(5,7,3,2,8,2,1,3) )
print( jumlah(100, 200, 300, 400, 500) )

def rata2(*args):
  hasil = 0
  for i in args:
    hasil += i
  return hasil / len(args)
   
print( rata2(5,7) )
print( rata2(5,7,3,2) )
print( rata2(5,7,3,2,8,2,1,3) )
print( rata2(100,200,300,400,500) )

# Pengertian Arbitrary Keyword Arguments (**kwargs) Python

# Jika dalam arbitrary arguments (*args) argumen fungsi ditulis
# langsung dengan nilai saja, maka dalam arbitrary
# keyword arguments (**kwargs), argumen fungsi tersebut ditulis
# dalam bentuk pasangan nama dan value. 

def sambung_kata(**kwargs):
  print(kwargs)
  print(type(kwargs))
 
sambung_kata(a="Belajar", b="Python", c="di", d="Duniailkom")

# Menampilkan Nilai **kwargs Fungsi Python

def sambung_kata(**kata):
  for i in kata:
     print(i)
 
sambung_kata(a="Belajar", b="Python", c="di", d="Duniailkom")

def sambung_kata(**kata):
  for i in kata.values():
     print(i)
 
sambung_kata(a="Belajar", b="Python", c="di", d="Duniailkom")

def sambung_kata(**kata):
  hasil = ""
  for i in kata.values():
     hasil += i + " "
  return hasil;
 
print( sambung_kata(a="Belajar", b="Python", c="di", d="Duniailkom") )

def test(var1, var2, *args,**kwargs):
  print(var1)
  print(var2)
  print(args)
  print(kwargs)
 
test(10, 20, 30, 40, 50, a = 60, b = 70, c = 80)


