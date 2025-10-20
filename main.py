import json
import os
from prettytable import PrettyTable

akun_file = 'P.DDP/PA/akun.json'
tol_file = 'P.DDP/PA/tol.json'
transaksi_file = 'P.DDP/PA/transaksi.json'

# === JSON HELPERS ===
def load_json(file):
    if not os.path.exists(file):
        return []
    with open(file, 'r') as f:
        return json.load(f)

def save_json(file, data):
    with open(file, 'w') as f:
        json.dump(data, f, indent=4)

# === MENU ADMIN ===
def menuAdmin(username):
    try:
        while True:
            print(f"\n=== MENU ADMIN (Login sebagai {username}) ===")
            print("[1] Lihat daftar ruas jalan tol")
            print("[2] Tambah ruas jalan tol")
            print("[3] Update ruas jalan tol")
            print("[4] Hapus ruas jalan tol")
            #print("[5] Lihat transaksi user")
            print("[0] Logout")

            adminInput = input("Pilih menu >>> ")

            # validasi input angka
            if not adminInput.isdigit():
                print("Input harus berupa angka!")
                continue

            adminInput = int(adminInput)

            # 1. Lihat Daftar Tol
            if adminInput == 1:
                data = load_json(tol_file)
                if not data:
                    print("Belum ada data ruas jalan tol.")
                else:
                    table = PrettyTable(["No", "Kode", "Nama", "Awal", "Tujuan", "Jarak(km)", "Tarif/km", "Status"])
                    for i, t in enumerate(data, start=1):
                        table.add_row([i, t["kode"], t["nama"], t["awal"], t["tujuan"], t["jarak"], t["tarif"], t["status"]])
                    print(table)

            # 2. Tambah Tol
            elif adminInput == 2:
                data = load_json(tol_file)
                kode = input("Masukan kode jalan tol: ")
                if any(t["kode"] == kode for t in data):
                    print("Kode jalan tol sudah ada")
                    continue
                nama = input("Masukkan nama jalan tol: ")
                awal = input("Masukkan kota awal: ")
                tujuan = input("Masukkan kota tujuan: ")
                jarak = float(input("Masukkan jarak (km): "))
                tarif = int(input("Masukkan tarif per km: "))
                status = input("Masukkan status (aktif/tutup): ")

                data.append({
                    "kode": kode, "nama": nama, "awal": awal,
                    "tujuan": tujuan, "jarak": jarak, "tarif": tarif, "status": status
                })
                save_json(tol_file, data)
                print("Data ruas jalan tol berhasil ditambahkan!")

            # 3. Update Tol
            elif adminInput == 3:
                try:
                    data = load_json(tol_file)
                    table = PrettyTable(["No", "Kode", "Nama"])
                    for i, t in enumerate(data, start=1):
                        table.add_row([i, t["kode"], t["nama"]])
                    print(table)
                    no = int(input("Masukkan nomor jalan tol yang ingin diubah: ")) - 1
                    if 0 <= no < len(data):
                        data[no]["nama"] = input("Nama baru: ")
                        data[no]["awal"] = input("Kota awal: ")
                        data[no]["tujuan"] = input("Kota tujuan: ")
                        data[no]["jarak"] = float(input("Jarak (km): "))
                        data[no]["tarif"] = int(input("Tarif per km: "))
                        data[no]["status"] = input("Status (aktif/tutup): ")
                        save_json(tol_file, data)
                        print("Data berhasil diperbarui!")
                    else:
                        print("Nomor tidak valid!")
                except ValueError:
                    print("Mohon inputkan value dengan benar")

            # 4. Hapus Tol
            elif adminInput == 4:
                try:
                    data = load_json(tol_file)
                    table = PrettyTable(["No", "Kode", "Nama"])
                    for i, t in enumerate(data, start=1):
                        table.add_row([i, t["kode"], t["nama"]])
                    print(table)
                    no = int(input("Masukkan nomor jalan tol yang ingin dihapus: ")) - 1
                    if 0 <= no < len(data):
                        hapus = data.pop(no)
                        save_json(tol_file, data)
                        print(f"Ruas '{hapus['nama']}' berhasil dihapus.")
                    else:
                        print("Nomor tidak valid!")
                except ValueError:
                    print("Mohon inputkan value dengan benar")
                
            # 5. Lihat Transaksi
            #elif adminInput == 5:
                

            # 0. Logout
            elif adminInput == 0:
                print("Logout admin...\n")
                break

            else:
                print("Pilihan tidak valid! Coba lagi.")

    except KeyboardInterrupt:
        print("\n\n💀 Program dihentikan paksa (Ctrl + C)")


# ================== MENU USER ==================
def menuUser(username):
    while True:
        akun = load_json(akun_file)
        saldo = next((a["saldo"] for a in akun if a["username"] == username), 0)

        print(f"\n=== MENU USER ({username}) ===")
        print(f"Saldo: Rp {saldo}")
        print("[1] Lihat daftar ruas tol")
        print("[2] Top up saldo")
        print("[3] Cek saldo")
        print("[4] Hitung & bayar tarif tol")
        print("[5] Lihat riwayat transaksi")
        print("[0] Logout")

        pilih = input("Pilih menu >>> ")

        # 1. Lihat daftar tol
        if pilih == "1":
            data = load_json(tol_file)
            table = PrettyTable(["No", "Kode", "Nama", "Awal", "Tujuan", "Jarak", "Tarif/km", "Status"])
            for i, t in enumerate(data, start=1):
                table.add_row([i, t["kode"], t["nama"], t["awal"], t["tujuan"], t["jarak"], t["tarif"], t["status"]])
            print(table)

        # 2. Top up saldo
        elif pilih == "2":
            nominal = int(input("Masukkan nominal top up: "))
            for a in akun:
                if a["username"] == username:
                    a["saldo"] += nominal
            save_json(akun_file, akun)
            print("Top up berhasil!")

        # 3. Cek saldo
        elif pilih == "3":
            print(f"Saldo Anda: Rp {saldo}")

        # 4. Hitung & bayar tol
        #elif pilih == "4":

        # 5. Lihat riwayat transaksi
        elif pilih == "5":
            transaksi = load_json(transaksi_file)
            user_trans = [t for t in transaksi if t["user"] == username]
            table = PrettyTable(["No", "Tol", "Golongan", "Jarak", "Total"])
            for i, t in enumerate(user_trans, start=1):
                table.add_row([i, t["tol"], t["golongan"], t["jarak"], t["total"]])
            print(table)

        elif pilih == "0":
            print("Logout berhasil.\n")
            break
        else:
            print("Pilihan tidak valid!")


# === LOGIN SYSTEM ===
def login_system():
    try:
        while True:
            print("\n===================")
            print("   SISTEM E-TOLL   ")
            print("===================")
            print("[1] Login")
            print("[2] Registrasi Akun")
            print("[0] Keluar")
            pilihan = input("Pilih menu >>> ")

            # Validasi input angka
            if not pilihan.isdigit():
                print("Input harus berupa angka!")
                continue

            pilihan = int(pilihan)

            # --- LOGIN ---
            if pilihan == 1:
                username = input("Masukkan username: ")
                password = input("Masukkan password: ")
                akun = load_json(akun_file)
                found = next((a for a in akun if a["username"] == username and a["password"] == password), None)

                if found:
                    print(f"\nHalo {username}, Anda login sebagai {found['role'].upper()}.")
                    if found["role"] == "admin":
                        menuAdmin(username)
                    else:
                        menuUser(username)
                else:
                    print("Username atau password salah!")
            
            elif pilihan == 2:
                akun = load_json(akun_file)
                username_baru = input("Buat username baru: ")

                if any(a["username"] == username_baru for a in akun):
                    print("Username sudah digunakan!")
                    continue

                password_baru = input("Buat password: ")
                role_baru = "user"

                akun.append({
                    "username": username_baru,
                    "password": password_baru,
                    "role": role_baru,
                    "saldo": 0
                })

                save_json(akun_file, akun)
                print(f"Akun '{username_baru}' berhasil dibuat!")

            # --- KELUAR PROGRAM ---
            elif pilihan == 0:
                print("Program ditutup.")
                break

            else:
                print("Pilihan tidak valid! Coba lagi.")

    except KeyboardInterrupt:
        print("\n\n💀 Program dihentikan paksa (Ctrl + C)")

# === MAIN PROGRAM ===
if __name__ == "__main__":
    login_system()
