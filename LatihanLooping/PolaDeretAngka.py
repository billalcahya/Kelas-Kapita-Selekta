print ("## Program Python Persegi Deret Angka ##")
print ("## ================================== ##")
print()

besar = int(input("Input besar persegi : "))

k = 1
for i in range (besar):
    for j in range (besar):
        print( f"{k:>2}" , end=" ", sep=" ")
        k = k + 1
    print()

print ("## Program Python Segitiga Deret Angka ##")
print ("## =================================== ##")
print()

tinggi = int(input("Input tinggi segitiga : "))

k = 1
for i in range (tinggi):
    for j in range (i+1):
        print(k, end=" ", sep=" ")
        k = k + 1
    print()


    