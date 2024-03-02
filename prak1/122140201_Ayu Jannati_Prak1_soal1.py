# Ayu Jannati Ali Putri
# 122140201
# Praktikum PBO RB

def masukkanBilanganBulat(prompt):
    # input bilangan bulat dengan prompt yang diberikan
    while True:
        try:
            userInput = int(input(prompt))
            return userInput
        except ValueError:
            print("Input tidak valid. Harap masukkan bilangan bulat.")

def hitungAngkaGanjil(batas_bawah, batas_atas):
    # menghitung jumlah bilangan ganjil sesuai rentang yang diberikan 
    if batas_bawah < 0 or batas_atas < 0:
        return "Batas bawah dan atas yang dimasukan tidak boleh di bawah Nol"

    total = 0
    angkaGanjil = []
    for num in range(batas_bawah, batas_atas):
        if num % 2 != 0:
            total += num
            angkaGanjil.append(num)

    return total, angkaGanjil

# mendapatkan input dari user
batas_bawah = masukkanBilanganBulat("Masukkan batas bawah : ")
batas_atas = masukkanBilanganBulat("Masukkan batas atas  : ")

# menampilkan hasil
hasil = hitungAngkaGanjil(batas_bawah, batas_atas)
if isinstance(hasil, tuple):
    total, angkaGanjil = hasil
    print(f"Total : {total}")
    print("Angka-angka ganjil dalam rentang :")
    for angka_ganjil in angkaGanjil:
        print(f"{angka_ganjil}")
else:
    print(hasil)  # menampilkan pesan kesalahan jika hasilnya bukan tuple