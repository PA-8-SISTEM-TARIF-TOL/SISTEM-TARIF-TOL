# 🚗 SISTEM TARIF TOL  

👥 **Anggota Kelompok 8 DDP:**  
- Harits (2509116048)  
- Ahmad Fajar Novia (2509116041)  
- Akhmad Rafliansyah (2509116045)  

---

## 📋 Deskripsi  
  Sistem tarif tol adalah program berbasis Python yang berfungsi untuk mengelola data ruas jalan tol serta menghitung biaya perjalanan secara otomatis berdasarkan jarak tempuh dan golongan kendaraan.
Sistem ini dibuat untuk memudahkan pengguna dalam melakukan pembayaran tol, sekaligus membantu admin dalam pengelolaan data jalan tol, tarif, dan riwayat transaksi.
Program ini memanfaatkan PrettyTable untuk menampilkan data dalam bentuk tabel yang terstruktur, pwinput untuk menjaga kerahasiaan input password, serta JSON sebagai media penyimpanan data.

---

## 🧑‍💼 Menu Admin  
1. Melihat daftar ruas jalan tol  
2. Menambahkan ruas jalan tol  
3. Update ruas jalan tol  
4. Hapus ruas jalan tol  
5. Lihat transaksi user  
6. Logout  

---

## 👥 Menu User  
1. Lihat daftar ruas jalan tol  
2. Top up saldo  
3. Cek saldo  
4. Hitung & bayar tarif tol  
5. Lihat riwayat transaksi  
6. Logout  

---

## ⚙️ Fitur dan Konsep Program  
Program dalam sistem tarif tol ini menggunakan berbagai konsep pemrograman, di antaranya:  
- **Tipe Data**  
- **Percabangan (if-else)**  
- **Perulangan (looping)**  
- **Function**  
- **CRUD (Create, Read, Update, Delete)**  
- **JSON**   
- **PrettyTable**  
- **pwinput**   
- **Error Handling**  

---
# 🗒️FLOWCHART SISTEM TARIF TOL

# Menu login

<img width="800" height="800" alt="1 drawio" src="https://github.com/user-attachments/assets/818e1ca5-951f-4639-af9b-a6f0c66bf9da" />

# Menu User

<img width="1516" height="1112" alt="2 drawio" src="https://github.com/user-attachments/assets/3b4e4b2f-4571-4aba-8127-48979a1dfb36" />
<img width="1391" height="1070" alt="3 drawio" src="https://github.com/user-attachments/assets/cded4fbb-b602-4078-87a1-e1ab37a22773" />

# Menu Admin

<img width="1723" height="1972" alt="4 drawio" src="https://github.com/user-attachments/assets/37b7503b-6b2b-4b7e-8782-d12981b5e690" />

---
## 🧭 Penjelasan Flowchart Sistem Tol  

### 1. Flowchart Login & Registrasi  

- **Login** → pengguna memasukkan username dan password untuk masuk.  
- **Registrasi** → pengguna membuat akun baru dengan mengisi username, password, dan konfirmasi password. Data disimpan ke file `akun.json`.  
- **Keluar** → menutup program.   

---

### 2. Flowchart Menu User    
- **Melihat daftar ruas jalan tol** (dibaca dari file `tol.json`).  
- **Melakukan top up saldo** ke akun (data disimpan di `akun.json`).  
- **Cek saldo** akun saat ini.  
- **Bayar tol** dengan memilih nomor jalan tol dan golongan kendaraan.  
- **Melihat riwayat transaksi** dari file `transaksi.json`.  
- **Keluar**
 

---

### 3. Flowchart Hitung & Bayar Tol  
1. User memilih nomor jalan tol.  
2. Program mengambil data jarak dan tarif per km dari `tol.json`.  
3. User memilih golongan kendaraan:  
   - Golongan 1 → harga normal.  
   - Golongan 2 → harga × 20%.  
   - Golongan 3 → harga × 40%.  
   - Golongan 4 → harga × 50%.  
4. Sistem menampilkan rincian biaya dan menanyakan konfirmasi pembayaran.  
5. Jika setuju, transaksi disimpan ke `transaksi.json` dan saldo user otomatis berkurang.
6. Jika tidak setuju, akan kembali ke menu user 

---

### 4. Flowchart Menu Admin  
- **Melihat daftar ruas jalan tol** lengkap dengan informasi kode, nama, kota asal-tujuan, jarak, tarif, dan status.  
- **Menambah data ruas jalan tol baru** (kode tidak boleh sama).  
- **Menghapus data jalan tol** (berdasarkan nomor data).  
- **Memperbarui data jalan tol** (mengubah nama, kota, jarak, tarif, atau status).  
- **Melihat transaksi user** yang tersimpan di `transaksi.json`.
- **Keluar**  

---
# 👨‍💻CODINGAN

```python
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
                    print("Terlalu banyak percobaan salah. Program dihentikan")
                    break


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

# === MAIN PROGRAM ===
if __name__ == "__main__":
    login_system()
```
# ▶️ CARA MENJALANKAN
1. Siapkan Python 3.8+
2. Buka aplikasi editor kode
3. Install dependensi di terminal
   ```
   pip install pwinput
   pip install prettytable
   ```
4. Masukan "main.py", "akun.json", "tol.json", "transaksi.json" dalam satu folder
5. Buka folder tersebut di aplikasi editor kode
6. Jalankan kode

# 📤 OUTPUT

## 👥 Regist Akun dan Login sebagai user
- jika anda belum mempunyai akun DETOL <br>
- Pilih menu 2 untuk melakukan regist akun terlebih dahulu <br>
- buat username baru<br>
- Buat password<br>
- Akun 'nama_akun' berhasil dibuat dan masuk dalam data akun.json <br>
- login dengan akun yang sudah dibuat kemudian menampilkan menu user<br>

---
<img width="865" height="906" alt="image" src="https://github.com/user-attachments/assets/5cb71072-c183-4cde-9bd5-8494dd220154" />

---
## 1️⃣ Menu 1 Sebagai user
jika anda ingin melihat kemana tujuan anda pada tol anda bisa mengikuti cara ini :
- input angka 1 pada tampilan menu user
- sistem akan melihatkan daftar ruas jalan tol
- user dapat melihat jalan tol yang aktif saja

---

<img width="716" height="598" alt="image" src="https://github.com/user-attachments/assets/5941400c-a0d7-46f1-9aa1-c959441d9629" />

---
## 2️⃣ Menu 2 Sebagai user
jika anda tidak mempunyai saldo e toll anda bisa top up dengan cara ini :
- input angka 2 pada tampilan menu user 
- menampilkan halaman top up
- masukkan nominal top up [min 1, max 2.000.000 ]
- input harus berupa angka jika tidak akan kembali ke menu user
- jika sudah maka, Top up berhasil!
---

<img width="657" height="857" alt="image" src="https://github.com/user-attachments/assets/a8c58908-a605-47dd-810f-70f39b87ed20" />

---
## 3️⃣ Menu 3 Sebagai user
jika anda lupa dengan saldo anda, anda bisa melihatnya denngan cara ini :
- input angka 3 pada tampilan menu user
- kemudian sistem akan menampilkan saldo anda yang tersimpan di akun.json
- Saldo Anda: Rp *****
---
  <img width="313" height="194" alt="image" src="https://github.com/user-attachments/assets/8b8ef3f8-36c2-4e62-8c15-bc9506452da8" />

---
## 4️⃣ Menu 4 Sebagai user
jika anda ingin membayar tol yang sudah anda lewati, dengan cara ini :
- input angka 4 pada tampilan menu user
- sistem akan menampilkan daftar ruas jalan tol
- masukkan no jalan tol yang anda lewati
- kemudian masukkan golongan kendaraan yang anda gunakan 
- beda golongan beda harga yang akan dibayar
- jika sudah memasukkan golongan maka sistem akan melihat apakah saldo anda cukup
- jika saldo tidak cukup maka akan menampilkan "Saldo idak cukup!"
- jika saldo cukup maka akan "Pembayaran berhasil! Total: Rp *****"

---
## 5️⃣ Menu 5 Sebagai user
jika anda ingin melihat hasil transaksi, dengan cara ini :
- input angka 5 pada tampilan menu user
- menampilkan hasil transaksi dari akun anda
- mulai dari nama user, nama tol, golongan, jarak dan total harga
- kemudian lansung kembali ke menu user

---

---![WhatsApp Image 2025-10-26 at 22 02 27](https://github.com/user-attachments/assets/8679d210-369b-44ee-84fd-42800399846d)

---
## 6️⃣ Menu 6 Sebagai user
jika anda ingin keluar dari tampilan user anda, dengan cara ini :
- input angka 6 pada tampilan menu user
- sistem akan meng log out akun anda
- dan akan menampilkan "Log out berhasil."
- kembali ke menu DETOL
---

<img width="638" height="552" alt="Screenshot 2025-10-26 201019" src="https://github.com/user-attachments/assets/c6bd84e7-a70b-4956-81d4-fa3097d94afd" />

---
## 🧑‍💼 Login sebagai admin
- input angka 1 pada tampilan menu DETOL
- masukkan username "admin1"
- masukkan password "1234"
- maka akan menampilkan halaman admin
---
<img width="435" height="567" alt="image" src="https://github.com/user-attachments/assets/b00143dc-a697-4040-b05a-aff7cbecc4a1" />

---
## 1️⃣ menu 1 sebagai admin
jika admin ingin melihat semua daftar jalan tol, dengan cara ini :
- input angka 1 pada tampilan menu admin
- sistem akan melihatkan daftar ruas jalan tol
- admin dapat melihat seluruh jalan tol yang aktif maupun yang tutup
---

<img width="883" height="469" alt="image" src="https://github.com/user-attachments/assets/896e7807-b62c-4c97-ae8e-c25baeecbb6b" />

---
## 2️⃣ menu 2 sebagai admin
jika admin ingin menambahkan ruas jalan tol baru, dengan cara ini :
- input angka 2 pada tampilan menu admin
- sistem akan menampilkan seluruh ruas jalan tol
- masukkan kode jalan tol **[jika sama maka akan disuruh input ulang kode]** 
- masukkan nama jalan tol
- masukkan kota awal
- masukkan kota tujuan
- masukkan jarak(km) **[wajib angka jika tidak maka akan disuruh input ulang]** 
- masukkan tarif/(km) **[wajib angka jika tidak maka akan disuruh input ulang]** 
- masukkan status jalan **[wajib input aktif/tutup jika maka akan disuruh input ulang]** 
- jika sudah semua di input sistem akan menampilkan "Data ruas jalan tol berhasil ditambahkan!"
- untuk melihatnya bisa ke menu admin 1
---
<img width="900" height="622" alt="Screenshot 2025-10-26 202408" src="https://github.com/user-attachments/assets/cde37e15-020b-4386-b9b8-e794fbef4439" />

<img width="861" height="519" alt="image" src="https://github.com/user-attachments/assets/15dab8c9-7f14-4eea-b23a-f91fda749acf" />

---
## 3️⃣ menu 3 sebagai admin
jika admin ingin mengubah ruas jalan tol yang sudah ada, dengan cara ini :
- input angka 3 pada tampilan menu admin
- sistem akan menampilkan seluruh ruas jalan tol
- masukkan no jalan tol yang ingin diubah [wajib ada di daftar jika tidak maka akan kembali ke menu admin]
- masukkan nama baru
- masukkan kota awal
- masukkan kota tujuan
- masukkan jarak(km) **[wajib angka jika tidak maka akan disuruh input ulang]** 
- masukkan tarif/(km) **[wajib angka jika tidak maka akan disuruh input ulang]** 
- masukkan status jalan **[wajib input aktif/tutup jika maka akan disuruh input ulang]** 
- jika sudah memasukkan semua maka akan menampilkan "Data berhasil diperbarui!"
---

<img width="790" height="705" alt="image" src="https://github.com/user-attachments/assets/2aac53bb-fc5c-42eb-9cf1-517f6406a8e3" />

---
## 4️⃣ menu 4 sebagai admin
jika admin ingin menghapus salah satu ruas jalan tol, dengan cara ini :
- input angka 4 pada tampilan menu admin
- sistem akan menampilkan no,kode dan nama jalan tol yang bisa dihapus
- masukkan no jalan tol yang ingin dihapus 
- jika no jalan tol tidak ada maka akan kembali ke menu admin
- jika no jalan tol ada, maka sistem akan menghapus ruas jalan tol
- dan menampilkan "Ruas '****' berhasil dihapus.
---

<img width="530" height="696" alt="image" src="https://github.com/user-attachments/assets/a8174b75-cccf-4c00-8032-e72e6ef0ee26" />

---
## 5️⃣ menu 5 sebagai admin
jika admin ingin melihat seluruh riwayat transaksi dari seluruh user yang sudah melakukan pembayaran, dengan cara ini :
- input angka 5 pada tampilan menu admin
- sistem akan menampilkan data transaksi dari seluruh user
---

<img width="725" height="353" alt="image" src="https://github.com/user-attachments/assets/fd8d8846-3072-4d7a-8f79-fe74964899f5" />

---
## 6️⃣ menu 6 sebagai admin
jika admin ingin keluar dari tampilan admin, dengan cara ini :
- input angka 6 pada tampilan menu admin
- sistem akan meng log out akun anda
- kembali ke menu DETOL

---
<img width="659" height="538" alt="image" src="https://github.com/user-attachments/assets/7fbc5cca-8b52-4048-9abb-d2dcb20c8b1b" />

---
## 🐞 Error Handling
Error handling pada program ini digunakan untuk mencegah program mengalami crash ketika terjadi kesalahan input atau gangguan dari pengguna.
### ✅ 1. Penanganan Input Bukan Angka (`ValueError`)
Digunakan ketika user memasukkan huruf atau simbol pada input yang seharusnya berupa angka. Program akan menampilkan pesan kesalahan tanpa berhenti secara tiba-tiba.
### ✅ 2. Penanganan Penghentian Mendadak (`KeyboardInterrupt`)
Ketika user menekan `Ctrl + C`, program menampilkan pesan yang sopan dan berhenti dengan aman.
### ✅ 3. Penanganan Input Terputus (`EOFError`)
Mencegah error ketika input kosong atau terputus, sehingga program tidak membeku.
### ✅ 4. Validasi Input Kosong
Program memastikan input tertentu (seperti nama, kode tol, kategori) tidak dalam keadaan kosong agar data tetap valid.
### ✅ 5. Validasi Range Angka
Mencegah input angka dengan nilai tidak logis, seperti jarak 0 atau negatif, tarif tidak valid, atau menu di luar pilihan.
### ✅ 6. Batas Maksimal Top Up
Program membatasi nominal top up agar tidak melebihi Rp 2.000.000 per transaksi, menyerupai sistem transaksi nyata.
### ✅ 7. Validasi Status Tol
Status hanya dapat berupa “aktif” atau “tutup”, sehingga tidak terjadi typo atau status tidak dikenal.
### ✅ 8. Validasi Kode Tol Duplikat
Mencegah kode jalan tol yang sama agar data tetap unik dan tidak membingungkan sistem.
### ✅ 9. Batas Percobaan Login
Pengguna hanya memiliki tiga kesempatan login untuk menjaga keamanan dan mencegah percobaan brute force.

---
## 📌 CONTOH
---
![WhatsApp Image 2025-10-26 at 21 36 50 (1)](https://github.com/user-attachments/assets/3a2c71c9-bd1e-45b8-bab6-efdf11fe688a)
![WhatsApp Image 2025-10-26 at 21 36 50](https://github.com/user-attachments/assets/bb08190b-6a26-4b0b-840c-f65429bf9807)
![WhatsApp Image 2025-10-26 at 21 36 49](https://github.com/user-attachments/assets/0b110e2e-d2fd-4b84-b498-9bd7e34a616f)

---

## 📚 Kesimpulan
---

Secara keseluruhan, program pembayaran tol berbasis Python yang saya buat ini berjalan dengan baik dan membantu pengguna melakukan transaksi e-toll secara lebih praktis. Fitur seperti cek saldo, top up, simulasi biaya sesuai golongan kendaraan, serta riwayat transaksi yang otomatis tersimpan dalam JSON membuat prosesnya lebih jelas dan tertata. Untuk Admin, tersedia pengelolaan data ruas tol lewat fitur CRUD serta pengecekan riwayat transaksi, sehingga pendataan menjadi lebih rapi. Dalam pengembangannya, saya menggunakan percabangan, perulangan, error handling, function, PrettyTable, dan keamanan password. Dengan semua fitur tersebut, program ini bisa menjadi simulasi layanan tol digital yang cukup efisien dan mudah dipahami.

---
<div align="center"> 

  ## 🙏TERIMA KASIH🤝 <br>
  
  Kami mengucapkan terima kasih kepada Asisten Laboratorium Konsultan dan Asisten Laboratorium yang telah memberikan arahan serta bimbingan selama proses pembuatan program ini.  Semoga project ini dapat bermanfaat dan menjadi pengalaman pembelajaran yang berharga.

</div>
