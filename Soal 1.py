#Menampilkan informasi program
print ("Menghitung Luas Persegi Panjang")

#Input nilai panjang dan lebar
P = float(input("Masukkan nilai panjang: "))
L = float(input("Masukkan nilai lebar: "))

#Menghitung luas persegi panjang
Luas_persegi_panjang = P * L

#Menampilkan hasil perhitungan luas persegi panjang
print ("Luas persegi panjang adalah",Luas_persegi_panjang)

#Menampilkan informasi Luas Lingkaran
print ("Menghitung Luas Lingkaran")

#Input nilai jari-jari
r = float(input("Masukkan nilai jari-jari: "))

#Menghitung luas lingkaran
Luas_lingkaran = 3.14 * (r ** 2)

#Menampilkan hasil perhitungan luas lingkaran
print ("Luas lingkaran adalah",Luas_lingkaran)

#Menampilkan informasi luas kubus
print ("Menghitung Luas Kubus")

#Input nilai sisi
s = float(input("Masukkan nilai sisi: "))

#Menghitung luas kubus
Luas_kubus = 6 * (s ** 2)

#Menampilkan hasil perhitungan luas kubus
print ("Luas kubus adalah",Luas_kubus)

#Menampilkan informasi pengkonversian suhu celcius ke farenheit
print ("Konversi Suhu Celcius ke Farenheit")

#Input nilai suhu dalam celcius
C = float(input("Masukkan nilai suhu dalam celcius: "))

#Menghitung hasil pengkonversian
C_F = 9 * (C + 32) / 5

#Menampilan hasil hitung pengkonversian
print ("Besar suhu celcius dalam Farenheit adalah",C_F, "F.")

#Menampilkan informasi pengkonversian suhu reamur ke kelvin
print ("Konversi Suhu Reamur ke Kelvin")

#Input nilai suhu dalam reamur
R = float(input("Masukkan nilai suhu dalam reamur: "))

#Menghitung hasil pengkonversian
R_K = 5 * (R + 273) / 4

#Menampilkan hasil hitung pengkonversian
print ("Besar suhu reamur dalam Kelvin adalah",R_K, "K.")
