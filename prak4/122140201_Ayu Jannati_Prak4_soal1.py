# Ayu Jannati Ali Putri
# 122140201
# Praktikum PBO 

''' 
catatan : modifikasi kodenya tidak langsung hasil output
tetapi terdapat input dari user dan 
apabila ingin diinputkan sesuai pada soal latihan hasilnya akan sama
'''

class Hewan:
    def _init_(self, nama, jenis_kelamin):
        self.nama = nama
        self.jenis_kelamin = jenis_kelamin

    def bersuara(self):
        pass

    def makan(self):
        pass

class Kucing(Hewan):
    def bersuara(self):
        print(f"Kucing {self.nama} bersuara : Meong!")

    def makan(self):
        print(f"Kucing {self.nama} sedang makan : tulang")

class Anjing(Hewan):
    def bersuara(self):
        print(f"Anjing {self.nama} bersuara : Guk Guk!")

    def makan(self):
        print(f"Anjing {self.nama} sedang makan : tulang")

# Input data dari pengguna
print("Masukkan Data Kucing")
nama_hewan1 = input("Nama Kucing : ")
jenis_kelamin_hewan1 = input("Jenis Kelamin Kucing : ")
print("==============================")
hewan1 = Kucing(nama_hewan1, jenis_kelamin_hewan1)

print("Masukkan Data Anjing")
nama_hewan2 = input("Nama Anjing : ")
jenis_kelamin_hewan2 = input("Jenis Kelamin Anjing : ")
print("==============================")
hewan2 = Anjing(nama_hewan2, jenis_kelamin_hewan2)

# Output
print(hewan1.nama)
print(hewan2.nama)
print("==============================")

hewan1.bersuara()
hewan1.makan()

hewan2.bersuara()
hewan2.makan()