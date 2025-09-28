<<<<<<< HEAD
# SOAL 1
# Lengkapilah class berikut agar program mencetak:
# Nama: Ani, Gaji: 8000000

class Karyawan:
    def __init__(self, nama, gaji):
        # Lengkapi di sini
        self.nama = nama
        self.gaji = gaji
        pass

    def tampilkan_info(self):
        # Lengkapi di sini
        print(f"Nama : {self.nama}, Gaji : {self.gaji}")
        pass

ani = Karyawan("Ani", 8000000)
ani.tampilkan_info()


# SOAL 2
# Modifikasi class berikut agar saldo tidak bisa diakses langsung,
# tapi bisa dilihat melalui method get_saldo() dan hanya bisa diubah
# dengan set_saldo(saldo_baru) jika saldo > 0.

class Rekening:
    def __init__(self, saldo):
        # Private attribute
        self.__saldo = saldo
        pass

    def get_saldo(self):
        return self.__saldo
        pass

    def set_saldo(self, saldo_baru):
        if saldo_baru > 0:
            self.__saldo = saldo_baru
        else:
            print("Saldo harus lebih dari 0")
        pass

r = Rekening(500)
print(r.get_saldo())  

r.set_saldo(1000)
print(r.get_saldo())  

r.set_saldo(-200)     
print(r.get_saldo()) 


# SOAL 3
# Buatlah class Orang dan Guru.
# Guru adalah subclass dari Orang.
# Orang punya atribut nama, Guru punya tambahan atribut mata_pelajaran.

# Dari ketentuan di atas, buatlah instance dari class Guru.
# Lalu cetak nama dan mata pelajaran dari instance Guru.
# Contoh:
#       Nama: Budi, Mengajar: Matematika

class Orang:
    def __init__(self,nama):
        self.nama = nama
        
class Guru(Orang):
    def __init__(self,nama,mata_pelajaran):
        super().__init__(nama)
        self.mata_pelajaran = mata_pelajaran
    
    def cetak(self):
        return (f"Nama : {self.nama} , Mengajar : {self.mata_pelajaran}")
    
guru1 = Guru("Budi","Matematika")
=======
# SOAL 1
# Lengkapilah class berikut agar program mencetak:
# Nama: Ani, Gaji: 8000000

class Karyawan:
    def __init__(self, nama, gaji):
        # Lengkapi di sini
        self.nama = nama
        self.gaji = gaji
        pass

    def tampilkan_info(self):
        # Lengkapi di sini
        print(f"Nama : {self.nama}, Gaji : {self.gaji}")
        pass

ani = Karyawan("Ani", 8000000)
ani.tampilkan_info()


# SOAL 2
# Modifikasi class berikut agar saldo tidak bisa diakses langsung,
# tapi bisa dilihat melalui method get_saldo() dan hanya bisa diubah
# dengan set_saldo(saldo_baru) jika saldo > 0.

class Rekening:
    def __init__(self, saldo):
        # Private attribute
        self.__saldo = saldo
        pass

    def get_saldo(self):
        return self.__saldo
        pass

    def set_saldo(self, saldo_baru):
        if saldo_baru > 0:
            self.__saldo = saldo_baru
        else:
            print("Saldo harus lebih dari 0")
        pass

r = Rekening(500)
print(r.get_saldo())  

r.set_saldo(1000)
print(r.get_saldo())  

r.set_saldo(-200)     
print(r.get_saldo()) 


# SOAL 3
# Buatlah class Orang dan Guru.
# Guru adalah subclass dari Orang.
# Orang punya atribut nama, Guru punya tambahan atribut mata_pelajaran.

# Dari ketentuan di atas, buatlah instance dari class Guru.
# Lalu cetak nama dan mata pelajaran dari instance Guru.
# Contoh:
#       Nama: Budi, Mengajar: Matematika

class Orang:
    def __init__(self,nama):
        self.nama = nama
        
class Guru(Orang):
    def __init__(self,nama,mata_pelajaran):
        super().__init__(nama)
        self.mata_pelajaran = mata_pelajaran
    
    def cetak(self):
        return (f"Nama : {self.nama} , Mengajar : {self.mata_pelajaran}")
    
guru1 = Guru("Budi","Matematika")
>>>>>>> ac458e39d145e283c523ef63805a7ff8fd2d0503
print(guru1.cetak())