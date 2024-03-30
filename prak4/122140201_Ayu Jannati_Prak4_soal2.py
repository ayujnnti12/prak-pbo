# Ayu Jannati Ali Putri
# 122140201
# Praktikum PBO RB

'''
catatan : modifikasi kodenya tidak langsung hasil output
tetapi terdapat input dari user dan 
apabila ingin diinputkan sesuai pada soal latihan hasilnya akan sama
'''

import math

class Persegi:
    def _init_(self, sisi):
        self.sisi = sisi

    def hitungLuas(self):
        luas = self.sisi ** 2
        return luas

class Lingkaran:
    def _init_(self, jari_jari):
        self.jari_jari = jari_jari

    def hitungLuas(self):
        luas = math.pi * (self.jari_jari ** 2)
        return luas

# Input data dari pengguna
print("===== Perhitungan Luas Persegi dan Lingkaran =====")
sisi_persegi = float(input("Masukkan Panjang Sisi Persegi : "))
jari_jari_lingkaran = float(input("Masukkan Jari-jari Lingkaran  : "))
print("=======================================")

# Membuat objek persegi dan lingkaran
persegi = Persegi(sisi_persegi)
lingkaran = Lingkaran(jari_jari_lingkaran)

# Output
luas_persegi = persegi.hitungLuas()
luas_lingkaran = lingkaran.hitungLuas()

if luas_persegi == int(luas_persegi):
    luas_persegi = int(luas_persegi)

print(f"Luas Persegi: {luas_persegi}")
print(f"Luas Lingkaran: {luas_lingkaran}")
print("=======================================")