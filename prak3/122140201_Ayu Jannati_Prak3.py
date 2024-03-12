# Ayu Jannati Ali Putri
# 122140201
# Praktikum PBO RB

class Dagangan:
    jumlah_barang = 0
    list_barang = []

    def __init__(self, nama, stok, harga):
        self.__nama = nama
        self.__stok = stok
        self.__harga = harga
        Dagangan.jumlah_barang += 1
        Dagangan.list_barang.append({'nama': self.__nama, 'stok': self.__stok, 'harga': self.__harga})

    def get_nama(self):
        return self.__nama

    def get_stok(self):
        return self.__stok

    def get_harga(self):
        return self.__harga

    def set_harga(self, harga):
        self.__harga = harga

    def tambah_stok(self, jumlah):
        self.__stok += jumlah

    def kurangi_stok(self, jumlah):
        if self.__stok >= jumlah:
            self.__stok -= jumlah
        else:
            print("Stok tidak mencukupi.")

    @staticmethod
    def lihat_barang():
        print("\nJumlah barang dagangan pada toko :", Dagangan.jumlah_barang, "buah")
        for barang in Dagangan.list_barang:
            print(f"{barang['nama']} seharga Rp {barang['harga']} (stok: {barang['stok']})")
        print("================================================")

# Contoh main program
Dagangan1 = Dagangan("Galon Aqua 19 L", 32, 17000)
Dagangan2 = Dagangan("Gas LPG 5 kg", 22, 88000)
Dagangan3 = Dagangan("Beras Ramos 5 kg", 13, 68000)

print("============ Program Daftar Dagangan ============")
Dagangan.lihat_barang()

del Dagangan1

print("\nGalon Aqua 19 L dihapus dari toko!")
Dagangan.jumlah_barang -= 1
Dagangan.list_barang = [barang for barang in Dagangan.list_barang if barang['nama'] != "Galon Aqua 19 L"]
Dagangan.lihat_barang()

del Dagangan2

print("\nGas LPG 5 kg dihapus dari toko!")
Dagangan.jumlah_barang -= 1
Dagangan.list_barang = [barang for barang in Dagangan.list_barang if barang['nama'] != "Gas LPG 5 kg"]
Dagangan.lihat_barang()

del Dagangan3

print("\nBeras Ramos 5 kg dihapus dari toko!")
Dagangan.jumlah_barang -= 1
Dagangan.list_barang = [barang for barang in Dagangan.list_barang if barang['nama'] != "Beras Ramos 5 kg"]
Dagangan.lihat_barang()