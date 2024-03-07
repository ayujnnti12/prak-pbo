# Ayu Jannati Ali Putri
# 122140201
# Praktikum PBO RB

def log_info(func):
    def wrapper(*args, **kwargs):
        print(f"Memanggil: {func.__name__}")
        return func(*args, **kwargs)
    return wrapper

class Murid:
    def __init__(self, nama, umur, disabilitas):
        self.nama = nama
        self.umur = umur
        self.disabilitas = disabilitas

    def __del__(self):
        print("Objek Murid", self.nama, "telah dihapus")

class SekolahDisabilitasLampung:
    def __init__(self, nama_sekolah, alamat):
        self.nama_sekolah = nama_sekolah
        self.alamat = alamat
        self.daftar_murid = []

    @log_info
    def tambah_murid(self):
        print("=" * 40)
        nama = input("Masukkan Nama Murid         : ")
        umur = input("Masukkan Umur Murid         : ")
        disabilitas = input("Masukkan Disabilitas Murid  : ")
        murid = Murid(nama, umur, disabilitas)
        self.daftar_murid.append(murid)

    @log_info
    def tampilkan_murid(self):
        print("=" * 40)
        print("Memanggil  : tampilkan_murid")
        print("=" * 40)
        print("Daftar Murid di Sekolah", self.nama_sekolah)
        for murid in self.daftar_murid:
            print("Nama        :", murid.nama)
            print("Umur        :", murid.umur)
            print("Disabilitas :", murid.disabilitas)
            print()

    def __del__(self):
        print("=" * 40)
        print("Objek Sekolah", self.nama_sekolah, "telah dihapus")

# Membuat objek sekolah
nama_sekolah = input("Masukkan Nama Sekolah     : ")
alamat_sekolah = input("Masukkan Alamat Sekolah   : ")
sekolah_disabilitas = SekolahDisabilitasLampung(nama_sekolah, alamat_sekolah)

# Menambahkan murid ke dalam sekolah
jumlah_murid = int(input("Jumlah Murid yang Ingin Ditambah : "))
for _ in range(jumlah_murid):
    sekolah_disabilitas.tambah_murid()

# Menampilkan informasi murid di sekolah
sekolah_disabilitas.tampilkan_murid()

# Menghapus objek sekolah
del sekolah_disabilitas