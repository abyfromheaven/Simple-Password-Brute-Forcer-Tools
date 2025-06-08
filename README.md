
# 🔓 UnlockKit - Python Brute Force Toolkit for ZIP and Beyond

**UnlockKit** adalah toolkit berbasis Python yang ringan dan edukatif, dirancang untuk membuka proteksi file yang dikunci dengan password menggunakan metode brute force. Versi awal mendukung cracking file ZIP dan akan dikembangkan untuk mendukung format lain seperti RAR, PDF, dan lainnya.

---

## 🧩 Fitur Utama

- 🚀 Brute force file ZIP menggunakan wordlist
- 📖 Input interaktif untuk file ZIP dan wordlist
- 🧱 Penanganan error yang lengkap dan aman
- 🔧 Mudah dimodifikasi dan dikembangkan untuk jenis file lain

---

## 📁 Struktur Direktori (Contoh)

```
UnlockKit/
├── tools/
│   └── zipcracker.py
├── wordlists/
│   └── example.txt
└── README.md
```

---

## 🧪 Contoh Penggunaan

### 1. Siapkan:
- File ZIP yang diproteksi, misal `protected.zip`
- File wordlist, misal `wordlists/example.txt`

### 2. Jalankan:
```bash
python3 tools/zipcracker.py
```

### 3. Input di terminal:
```
Masukkan path ke file ZIP: protected.zip
Masukkan path ke file wordlist: wordlists/example.txt
```

Jika password ditemukan, akan muncul:
```
[+] Kata sandi ditemukan: [password]
```

Jika tidak ditemukan:
```
[-] Kata sandi tidak ditemukan dalam wordlist.
```

---

## 🛠️ Penjelasan Script: `zipcracker.py`

File utama `zipcracker.py` terdiri dari dua fungsi:

### 🔐 `brute_force_zip(zip_file_path, wordlist_file_path)`
Melakukan brute force terhadap file ZIP dengan mencoba semua kata dalam wordlist.

### 🧭 `main()`
Menjalankan interaksi CLI dan memulai proses brute force.

---

## 📌 Catatan

- ❗ **Hanya digunakan untuk pembelajaran atau pengujian keamanan milik pribadi.**
- 🚫 Jangan gunakan tool ini untuk aktivitas ilegal.
- 🧠 Sangat cocok untuk pemula Python & Cyber Security.

---

## 📈 Roadmap Pengembangan

- [ ] Tambahkan dukungan file RAR (`rarfile`)
- [ ] Tambahkan dukungan file PDF (`pikepdf`)
- [ ] GUI mode dengan Tkinter atau CustomTkinter
- [ ] Web UI dengan Flask
- [ ] Mode multi-threaded untuk kecepatan

---

## 📦 Requirements

- Python 3.x
- Tidak memerlukan library eksternal (untuk `zipcracker.py`)

---

## 👨‍💻 Kontribusi

Pull request, issue, dan saran sangat diterima!  
Tool ini dirancang sebagai tempat belajar dan eksplorasi dunia *brute force* dan *file cracking* yang aman.

---

## 📝 Lisensi

Proyek ini dilisensikan di bawah [MIT License](https://opensource.org/licenses/MIT).

---

## 🙏 Kredit

Dibuat oleh: **Muhammad Abiyan Hafidz**  
Sebagai bagian dari eksplorasi dunia **Cyber Security & Python Tools**.
