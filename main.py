import json
import os
import pwinput
from prettytable import PrettyTable

akun_file = 'akun.json'
tol_file = 'tol.json'
transaksi_file = 'transaksi.json'

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
    while True:
        try:
            print(f"\n=== MENU ADMIN (Login sebagai {username}) ===")
            print("[1] Lihat daftar ruas jalan tol")
            print("[2] Tambah ruas jalan tol")
            print("[3] Update ruas jalan tol")
            print("[4] Hapus ruas jalan tol")
            print("[5] Lihat transaksi user")
            print("[6] Logout")

            adminInput = int(input("Pilih menu >>> "))

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
                if not data:
                    print("Belum ada data ruas jalan tol.")
                    continue

                table = PrettyTable(["No", "Kode", "Nama", "Awal", "Tujuan", "Jarak", "Tarif", "Status"])
                for i, t in enumerate(data, start=1):
                    table.add_row([i, t["kode"], t["nama"], t["awal"], t["tujuan"], t["jarak"], t["tarif"], t["status"]])
                print(table)

                while True:
                    kode = input("Masukkan kode jalan tol: ").strip()
                    if kode == "":
                        print("Input tidak boleh kosong!")
                        continue
                    if any(t["kode"] == kode for t in data):
                        print("Kode jalan tol sudah ada!")
                        continue
                    break

                while True:
                    nama = input("Masukkan nama jalan tol: ").strip()
                    if nama == "":
                        print("Input tidak boleh kosong!")
                    else:
                        break

                while True:
                    awal = input("Masukkan kota awal: ").strip()
                    if awal == "":
                        print("Input tidak boleh kosong!")
                    else:
                        break

                while True:
                    tujuan = input("Masukkan kota tujuan: ").strip()
                    if tujuan == "":
                        print("Input tidak boleh kosong!")
                    else:
                        break

                while True:
                    try:
                        jarak = float(input("Masukkan jarak (km): "))
                        if jarak <= 0:
                            print("Jarak harus lebih dari 0!")
                            continue
                        break
                    except ValueError:
                        print("Harus berupa angka!")

                while True:
                    try:
                        tarif = int(input("Masukkan tarif per km: "))
                        if tarif <= 0:
                            print("Tarif harus lebih dari 0!")
                            continue
                        break
                    except ValueError:
                        print("Harus berupa angka!")

                while True:
                    status = input("Masukkan status (aktif/tutup): ").strip().lower()
                    if status not in ["aktif", "tutup"]:
                        print("Status hanya boleh 'aktif' atau 'tutup'")
                    else:
                        break

                data.append({
                    "kode": kode,
                    "nama": nama,
                    "awal": awal,
                    "tujuan": tujuan,
                    "jarak": jarak,
                    "tarif": tarif,
                    "status": status
                })
                save_json(tol_file, data)
                print("Data ruas jalan tol berhasil ditambahkan!")

            # 3. Update Tol
            elif adminInput == 3:
                data = load_json(tol_file)
                if not data:
                    print("Belum ada data ruas jalan tol.")
                    continue

                table = PrettyTable(["No", "Kode", "Nama", "Awal", "Tujuan", "Jarak", "Tarif", "Status"])
                for i, t in enumerate(data, start=1):
                    table.add_row([i, t["kode"], t["nama"], t["awal"], t["tujuan"], t["jarak"], t["tarif"], t["status"]])
                print(table)

                try:
                    no = int(input("Masukkan nomor jalan tol yang ingin diubah: ")) - 1
                except:
                    print("Input harus angka!")
                    continue

                if not (0 <= no < len(data)):
                    print("Nomor tidak valid!")
                    continue

                nama_baru = input(f"Nama baru ({data[no]['nama']}): ").strip()
                if nama_baru != "":
                    data[no]["nama"] = nama_baru

                awal_baru = input(f"Kota awal baru ({data[no]['awal']}): ").strip()
                if awal_baru != "":
                    data[no]["awal"] = awal_baru

                tujuan_baru = input(f"Kota tujuan baru ({data[no]['tujuan']}): ").strip()
                if tujuan_baru != "":
                    data[no]["tujuan"] = tujuan_baru

                while True:
                    jarak_baru = input(f"Jarak baru ({data[no]['jarak']} km): ").strip()
                    if jarak_baru == "":
                        break
                    try:
                        data[no]["jarak"] = float(jarak_baru)
                        break
                    except:
                        print("Jarak harus angka!")

                while True:
                    tarif_baru = input(f"Tarif per km baru ({data[no]['tarif']}): ").strip()
                    if tarif_baru == "":
                        break
                    try:
                        data[no]["tarif"] = int(tarif_baru)
                        break
                    except:
                        print("Tarif harus angka!")

                while True:
                    status_baru = input(f"Status baru ({data[no]['status']}): ").strip().lower()
                    if status_baru == "":
                        break
                    if status_baru in ["aktif", "tutup"]:
                        data[no]["status"] = status_baru
                        break
                    print("Status hanya boleh 'aktif' atau 'tutup'")

                save_json(tol_file, data)
                print("Data berhasil diperbarui!")


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
            elif adminInput == 5:
                transaksi = load_json(transaksi_file)

                if not transaksi:
                    print("Belum ada transaksi.")
                    continue

                table = PrettyTable(["No", "User", "Tol", "Golongan", "Jarak", "Total"])
                for i, t in enumerate(transaksi, start=1):
                    table.add_row([i, t["user"], t["tol"], t["golongan"], t["jarak"], t["total"]])

                print(table)

            # 0. Logout
            elif adminInput == 6:
                print("Logout admin...\n")
                break

            else:
                print("Pilihan tidak tersedia")
                
        except KeyboardInterrupt:
            print("\nProgram dihentikan paksa")
            break
        except EOFError:
            print("Input tidak diterima")
        except ValueError:
            print("\nInput harus brupa angka\n")
            continue


# ================== MENU USER ==================
def menuUser(username):
    while True:
        try:
            akun = load_json(akun_file)
            saldo = next((a["saldo"] for a in akun if a["username"] == username), 0)

            print(f"\n=== MENU USER ({username}) ===")
            print(f"Saldo: Rp {saldo}")
            print("[1] Lihat daftar ruas tol")
            print("[2] Top up saldo")
            print("[3] Cek saldo")
            print("[4] Hitung & bayar tarif tol")
            print("[5] Lihat riwayat transaksi")
            print("[6] Log out")

            pilih = int(input("Pilih menu >>> "))

            # 1. Lihat daftar tol
            if pilih == 1:
                data = load_json(tol_file)
                aktif = [t for t in data if t["status"].lower() == "aktif"]

                if not aktif:
                    print("Tidak ada ruas tol yang aktif saat ini.")
                    continue

                table = PrettyTable(["No", "Kode", "Nama", "Awal", "Tujuan", "Jarak", "Tarif/km"])
                for i, t in enumerate(aktif, start=1):
                    table.add_row([i, t["kode"], t["nama"], t["awal"], t["tujuan"], t["jarak"], t["tarif"]])
                print(table)


            # 2. Top up saldo
            elif pilih == 2:
                try:
                    nominal = int(input("Masukkan nominal top up: "))
                except:
                    print("Input harus angka")
                    continue

                if nominal <= 0:
                    print("Nominal harus lebih dari 0")
                    continue

                akun = load_json(akun_file)
                for a in akun:
                    if a["username"] == username:
                        saldo_sekarang = a["saldo"]
                        break


                if nominal > 2000000:
                    print("Maksimal top up per transaksi adalah Rp 2.000.000")
                    continue

                for a in akun:
                    if a["username"] == username:
                        a["saldo"] += nominal
                
                save_json(akun_file, akun)
                print("Top up berhasil!")


            # 3. Cek saldo
            elif pilih == 3:
                print(f"Saldo Anda: Rp {saldo}")

            # 4. Hitung & bayar tol
            elif pilih == 4:
                data = load_json(tol_file)
                aktif = [t for t in data if t["status"].lower() == "aktif"]

                if not aktif:
                    print("Tidak ada tol aktif untuk digunakan.")
                    continue

                table = PrettyTable(["No", "Kode", "Nama", "Awal", "Tujuan", "Jarak", "Tarif/km"])
                for i, t in enumerate(aktif, start=1):
                    table.add_row([i, t["kode"], t["nama"], t["awal"], t["tujuan"], t["jarak"], t["tarif"]])
                print(table)

                try:
                    no = int(input("Masukkan nomor tol: ")) - 1
                except:
                    print("Input harus angka!")
                    continue

                if not (0 <= no < len(aktif)):
                    print("Nomor tidak valid!")
                    continue

                tol = aktif[no]

                jarak = tol["jarak"]

                print("Golongan kendaraan:")
                print("[1] Roda 4 (+0%)")
                print("[2] Roda 6 (+20%)")
                print("[3] Roda 8 (+40%)")
                print("[4] Roda >8 (+50%)")

                try:
                    gol = int(input("Pilih golongan: "))
                    faktor = [1, 1.2, 1.4, 1.5][gol - 1]
                except:
                    print("Input golongan tidak valid!")
                    continue

                total = jarak * tol["tarif"] * faktor

                if saldo >= total:
                    for a in akun:
                        if a["username"] == username:
                            a["saldo"] -= total
                    save_json(akun_file, akun)

                    transaksi = load_json(transaksi_file)
                    transaksi.append({
                        "user": username,
                        "tol": tol["nama"],
                        "golongan": gol,
                        "jarak": jarak,
                        "total": total
                    })
                    save_json(transaksi_file, transaksi)

                    print(f"Pembayaran berhasil! Total: Rp {total:,.0f}")
                else:
                    print("Saldo tidak cukup!")


            # 5. Lihat riwayat transaksi
            elif pilih == 5:
                transaksi = load_json(transaksi_file)

                if not transaksi:
                    print("Belum ada data transaksi.")
                    continue
                    
                table = PrettyTable(["No", "User", "Tol", "Golongan", "Jarak", "Total"])

                for i, t in enumerate(transaksi, start=1):
                    table.add_row([i, t["user"], t["tol"], t["golongan"], t["jarak"], t["total"]])

                print(table)

            elif pilih == 6:
                print("Log out berhasil.\n")
                break

            else:
                print("Pilihan tidak tersedia")

                
        except KeyboardInterrupt:
            print("\nInput tidak diterima. Gunakan menu Logout")
        except EOFError:
            print("\nInput tidak diterima")
        except ValueError:
            print("\nInput harus brupa angka\n")
            continue


# === LOGIN SYSTEM ===
def login_system():
    while True:
        try:
            print("\n===================")
            print("   SISTEM E-TOLL   ")
            print("===================")
            print("[1] Login")
            print("[2] Registrasi Akun")
            print("[3] Keluar")

            pilihan = int(input("Pilih menu >>> "))

            # 1. Login
            if pilihan == 1:
                attempts = 0
                while attempts < 3:
                    username = input("Masukkan username: ")
                    password = pwinput.pwinput(prompt="Masukkan password: ")

                    akun = load_json(akun_file)
                    found = next((a for a in akun if a["username"] == username and a["password"] == password), None)

                    if found:
                        print(f"\nHalo {username}, Anda login sebagai {found['role'].upper()}.")
                        if found["role"] == "admin":
                            menuAdmin(username)
                        else:
                            menuUser(username)
                        break

                    else:
                        attempts += 1
                        print(f"Username atau password salah! Percobaan ke {attempts}/3")

                if attempts == 3:
                    print("Terlalu banyak percobaan. Kembali ke menu awal.")


            # 2. Regist Akun
            elif pilihan == 2:
                akun = load_json(akun_file)

                username_baru = input("Buat username baru: ").strip()
                if username_baru == "":
                    print("Username tidak boleh kosong!")
                    continue

                if any(a["username"] == username_baru for a in akun):
                    print("Username sudah digunakan!")
                    continue

                password_baru = input("Buat password: ").strip()
                if password_baru == "":
                    print("Password tidak boleh kosong!")
                    continue

                role_baru = "user"

                akun.append({
                    "username": username_baru,
                    "password": password_baru,
                    "role": role_baru,
                    "saldo": 0
                })

                save_json(akun_file, akun)
                print(f"Akun '{username_baru}' berhasil dibuat!")


            # 3. Keluar pr0gram
            elif pilihan == 3   :
                print("Program ditutup.")
                break

            else:
                print("Pilihan tidak tersedia")

        except KeyboardInterrupt:
            print("\nProgram dihentikan paksa")
            break
        except EOFError:
            print("\nInput tidak diterima")
            continue
        except ValueError:
            print("\nInput harus berupa angka")
            continue

# === Startup ===
def start():
    while True:
        try:
            print("============================================")
            print("[     _____  ______ _______ ____  _         ")
            print("[    |  __ \|  ____|__   __/ __ \| |        ")
            print("[    | |  | | |__     | | | |  | | |        ")
            print("[    | |  | |  __|    | | | |  | | |        ")
            print("[    | |__| | |____   | | | |__| | |____    ")
            print("[    |_____/|______|  |_|  \____/|______|   ")
            print("[                                           ")
            print("============================================")
            print("Dashboard E-Toll Transaksi Otomatis Langsung")
            print("============================================")
            print("[1] Mulai Program")
            print("[2] Tutup Program")

            option = int(input(">>> "))

            if option == 1:
                login_system()
            elif option == 2:
                print("Program ditutup")
                exit()
                
            elif option == 3:
                print("[MOD]")
                print("VIEW ALL JSON")

                akun = load_json(akun_file)
                tol = load_json(tol_file)
                transaksi = load_json(transaksi_file)

                tableA = PrettyTable(["No", "Username", "Password", "Role", "Saldo"])
                for i, t in enumerate(akun, start=1):
                    tableA.add_row([i, t["username"], t["password"], t["role"], t["saldo"]])
                    
                tableTol = PrettyTable(["No", "Kode", "Nama", "Awal", "Tujuan", "Jarak", "Tarif", "Status"])
                for i, t in enumerate(tol, start=1):
                    tableTol.add_row([i, t["kode"], t["nama"], t["awal"], t["tujuan"], t["jarak"], t["tarif"], t["status"]])
                    
                tableT = PrettyTable(["No", "User", "Tol", "Golongan", "Jarak", "Total"])
                for i, t in enumerate(transaksi, start=1):
                    tableT.add_row([i, t["user"], t["tol"], t["golongan"], t["jarak"], t["total"]])

                print(tableA)
                print(tableTol)
                print(tableT)
                
            else:
                print("Pilihan tidak valid! Coba lagi\n")

        except KeyboardInterrupt:
            print("\nKeyboardInterrupt terdeteksi. Kembali ke menu awal\n")
            continue
        except EOFError:
            print("\nEOFError terdeteksi. Mohon ulangi lagi input\n")
            continue
        except ValueError:
            print("\nInput harus brupa angka\n")
            continue


# === MAIN PROGRAM ===
if __name__ == "__main__":
    start()
