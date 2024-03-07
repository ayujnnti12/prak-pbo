# Ayu Jannati Ali Putri
# 122140201
# Praktikum PBO RB

class Mahasiswa:
    def __init__(self, nim, nama, angkatan, isMahasiswa = True):
        self.__nim = nim
        self.__nama = nama
        self.angkatan = angkatan
        self.isMahasiswa = isMahasiswa

    def get_nim(self):
        return self.__nim

    def set_nim(self, nim):
        self.__nim = nim

    def get_nama(self):
        return self.__nama

    def set_nama(self, nama):
        self.__nama = nama

    def get_angkatan(self):
        return self.angkatan

    def is_mahasiswa(self):
        return self.isMahasiswa

# Inisialisasi objek pertama dengan semua parameter
mahasiswa1 = Mahasiswa("122140201", "Ayu Jannati", 2022, True)

# Inisialisasi objek kedua tanpa parameter isMahasiswa (menggunakan default value)
mahasiswa2 = Mahasiswa("122140202", "Janna Putri", 2023)

print("NIM Mahasiswa 1       :", mahasiswa1.get_nim())
print("Nama Mahasiswa 1      :", mahasiswa1.get_nama())
print("Angkatan Mahasiswa 1  :", mahasiswa1.get_angkatan())
print("Apakah Mahasiswa 1 adalah mahasiswa?", mahasiswa1.is_mahasiswa())

# Tambahan pemisah
print("\n" + "=" * 42)

# Mengganti nama dan nim mahasiswa kedua menggunakan setter
mahasiswa2.set_nim("122140202")
mahasiswa2.set_nama("Janna Putri")

print("\nNIM Mahasiswa 2       :", mahasiswa2.get_nim())
print("Nama Mahasiswa 2      :", mahasiswa2.get_nama())
print("Angkatan Mahasiswa 2  :", mahasiswa2.get_angkatan())
print("Apakah Mahasiswa 2 adalah mahasiswa?", mahasiswa2.is_mahasiswa())