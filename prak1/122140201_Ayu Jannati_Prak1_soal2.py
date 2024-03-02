# Ayu Jannati Ali Putri
# 122140201
# Praktikum PBO RB 

import math
pi = 3.14

def menghitungLuasLingkaran(jari_jari):
    # menghitung luas lingkaran sesuai jari-jari yang diinputkan
    return pi * jari_jari**2

def menghitungKelilingLingkaran(jari_jari):
    # menghitung keliling lingkaran sesuai jari-jari yang diinputkan
    return 2 * pi * jari_jari

def masukkanJariJari():
    # input jari-jari oleh pengguna
    while True:
        try:
            jari_jari = int(input("Masukkan jari-jari lingkaran : "))
            if jari_jari < 0:
                print("Jari-jari lingkaran tidak boleh negatif")
            else:
                return jari_jari
        except ValueError:
            print("Input tidak valid. Harap masukkan bilangan positif")

# input dari pengguna
jari_jari = masukkanJariJari()

# menghitung luas dan keliling lingkaran sesuai input jari-jari 
luas = menghitungLuasLingkaran(jari_jari)
keliling = menghitungKelilingLingkaran(jari_jari)

# menampilkan hasil
print(f"Luas lingkaran dengan jari-jari {jari_jari} adalah     : {luas}")
print(f"Keliling lingkaran dengan jari-jari {jari_jari} adalah : {keliling}")