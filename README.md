# SISTEM-TARIF-TOL
- Harits 2509116048 | - Ahmad Fajar Novia 2509116041 | - Akhmad Rafliansyah 2509116045


Sistem tarif tol ini merupakan sistem yang mengelola data pada ruas jalan tol , menggunakan PrettyTable untuk tampilan tabel yang rapi menggunakan pwinput dan  JSON untuk penyimpanan data.
Sistem ini memiliki dua peran utama, yaitu Admin dan User, dengan fungsi dan hak akses yang berbeda.
Menu Admin
1. Melihat ruas jalan tol
2. menambahkan ruas jalan tol
3. update ruas jalan tol
4. hapus ruas jalan tol
5. lihat transaksi user
6. logout

Menu user
1. lihat daftar ruas jalan tol
2. top up saldo
3. cek saldo
4. hitung & bayar tarif tol
5. lihat riwayat transaksi
6. logout

Program yang ada pada sistem tarif tol
- Tipe data
- percabangan
- Perulangan
- function
- CRUD
- JSON
- Prettytable
- pwinput
- Errorhandling


---
# FLOWCHART SISTEM TARIF TOL

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
Flowchart ini menjelaskan proses awal ketika program dijalankan.  
Pengguna akan masuk ke **menu login** yang berisi tiga pilihan:  
- **Login** → pengguna memasukkan username dan password untuk masuk.  
- **Registrasi** → pengguna membuat akun baru dengan mengisi username, password, dan konfirmasi password. Data disimpan ke file `akun.json`.  
- **Keluar** → menutup program.  

Jika username dan password cocok, pengguna diarahkan ke menu sesuai perannya (**Admin** atau **User**).  

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
- **Menambah data ruas jalan tol baru** (dengan validasi agar kode tidak duplikat).  
- **Menghapus data jalan tol** berdasarkan nomor.  
- **Memperbarui data jalan tol** (mengubah nama, kota, jarak, tarif, atau status).  
- **Melihat transaksi user** yang tersimpan di `transaksi.json`.
- **Keluar**  




# CODINGAN



