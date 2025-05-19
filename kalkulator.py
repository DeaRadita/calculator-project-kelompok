from operasi import tambah, kurang, kali, bagi

print("APLIKASI KALKULATOR SEDERHANA")
print("1. Tambah")
print("2. Kurang")
print("3. Kali")
print("4. Bagi")

pilih = input("Pilih operasi (1/2/3/4): ")
a = float(input("Masukkan angka pertama: "))
b = float(input("Masukkan angka kedua: "))

if pilih == '1':
    print("Hasil:", tambah(a, b))
elif pilih == '2':
    print("Hasil:", kurang(a, b))
elif pilih == '3':
    print("Hasil:", kali(a, b))
elif pilih == '4':
    print("Hasil:", bagi(a, b))
else:
    print("Pilihan tidak valid")

