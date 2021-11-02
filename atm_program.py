import datetime
import random
import os
from customer import Customer

atm = Customer(id)
title = """\033[92m
  /$$$$$$  /$$$$$$$$ /$$      /$$
 /$$__  $$|__  $$__/| $$$    /$$$
| $$  \ $$   | $$   | $$$$  /$$$$
| $$$$$$$$   | $$   | $$ $$/$$ $$
| $$__  $$   | $$   | $$  $$$| $$
| $$  | $$   | $$   | $$\  $ | $$
| $$  | $$   | $$   | $$ \/  | $$
|__/  |__/   |__/   |__/     |__/\033[93m Progate\033[00m
"""

while True:
    os.system("cls")
    print(title)
    id = int(input("Masukan 6 Digit Pin Anda : "))
    chances = 0

    while (id != int(atm.checkPin()) and chances < 3):
        id = int(input("Pin Anda Salah! Silahkan Masukan Lagi : "))
        chances += 1

        if chances == 3:
            print("Error! Silahkan Ambil Kartu dan Coba Lagi..")
            exit()
    
    while True:
        print("=" * 55 + "\n")
        print("Selamat Datang di ATM Progate..")
        print("\n 1 - Cek Saldo     2 - Debet     3 - Simpan \n 4 - Ganti Pin     5 - Keluar")
        choose = int(input("\nSilahkan Pilih Menu : "))

        if choose == 1:
            print("\nSaldo Anda Sekarang : Rp", f"{(atm.checkBalance()):,}".replace(',', '.') + "\n")

        elif choose == 2:
            nominal = int(input("\nMasukan Nominal Saldo : Rp "))
            verify_withdraw = input("Konfirmasi : Anda Akan Melakukan Debet Dengan Nominal Rp " +  f"{(nominal):,}".replace(',', '.') + "\n(y/n) : ")
            # verify_withdraw = input("Konfirmasi : Anda Akan Melakukan Debet Dengan Nominal " + str(nominal) + "\n(y/n) : ")

            if verify_withdraw == "y" or verify_withdraw == "Y":
                print("Saldo Awal Anda Adalah : Rp",  f"{(atm.checkBalance()):,}".replace(',', '.') + "\n")
            else:
                break
            if nominal < atm.checkBalance():
                atm.withdrawBalance(nominal)
                print("Transaksi Debet Berhasil!")
                print("Saldo Anda Sekarang    : Rp",  f"{(atm.checkBalance()):,}".replace(',', '.') + "\n")
            else:
                print("Maaf. Saldo Anda Tidak Cukup Untuk Melakukan Debet!")
                print("Silahkan Lakukan Penambahan Nominal Saldo")

        elif choose == 3:
            nominal = int(input("\nMasukan Nominal Saldo : Rp "))
            verify_deposit = input("Konfirmasi : Anda Akan Melakukan Penyimpanan Dengan Nominal Rp " + f"{(nominal):,}".replace(',', '.') + "\n(y/n) : ")

            if verify_deposit == "y" or verify_deposit == "Y":
                atm.depositBalance(nominal)
                print("Saldo Anda Sekarang Adalah : Rp", str(atm.checkBalance()) + "\n")
            else:
                break

        elif choose == 4:
            verify_pin = int(input("\nMasukan Pin Anda : "))

            while verify_pin != int(atm.checkPin()):
                print("Pin Anda Salah!")
                verify_pin = int(input("\nMasukan Pin Anda : "))

            update_pin = int(input("Silahkan Masukan Pin Baru : "))
            print("Pin Anda Berhasil Diganti!")

            verify_newpin = int(input("Coba Masukan Pin Baru: "))

            if verify_newpin == update_pin:
                print("Pin Baru Anda Sukses!" + "\n")
            else:
                print("Maaf. Pin Anda Salah" + "\n")
            
        elif choose == 5:
            print("\nResi Tercetak Otomatis Saat Anda Keluar. \nHarap Simpan Tanda Terima Ini Sebagai Bukti Transaksi Anda!")
            print("-" * 55)
            date = datetime.datetime.now()
            print("Tanggal      :", date.strftime('%A %d/%m/%Y %H:%M:%S'))
            print("No. Record   :", random.randint(100000, 1000000))
            print("Saldo Akhir  :", f"Rp {(atm.checkBalance()):,}".replace(',', '.'))
            print("Terima Kasih Telah Menggunakan ATM Progate")
            print("-" * 55 + "\n")
            exit()

        else:
            print("Error. Maaf, Menu Tidak Tersedia")
