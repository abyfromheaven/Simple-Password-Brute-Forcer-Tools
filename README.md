Simple Password Brute-Forcer Tools (ZIP Edition & Beyond)
Ini adalah koleksi tools sederhana berbasis Python yang dapat digunakan untuk brute force password pada berbagai jenis file yang dilindungi, dimulai dari file ZIP. Tools ini dirancang untuk belajar dasar serangan brute force dan pemrosesan file di Python, serta bisa dikembangkan untuk jenis file lainnya (seperti RAR, PDF, dll.).

✨ Fitur Utama
🔓 Brute-force password file ZIP menggunakan wordlist.

📁 Mendukung wordlist eksternal (.txt) dengan encoding fleksibel.

⚠️ Menangani error umum: file tidak ditemukan, format rusak, dll.

🔧 Mudah dikembangkan untuk jenis file atau serangan lainnya.

📁 Saat Ini: zipcracker.py - Brute Forcer ZIP
🔍 Deskripsi
Script zipcracker.py digunakan untuk mencoba membuka file ZIP yang diproteksi dengan password menggunakan metode brute force dari daftar kata sandi (wordlist).

🧠 Cara Kerja Singkat
Meminta path file ZIP dan file wordlist dari user.

Membuka file ZIP.

Membaca setiap baris dari wordlist.

Mencoba mengekstrak file ZIP dengan password tersebut.

Jika berhasil → Password ditampilkan.

Jika gagal → Mencoba password berikutnya sampai akhir wordlist.

🧪 Contoh Penggunaan
🔧 Persiapan:
Buat file ZIP yang dipassword: protected.zip

Siapkan file wordlist: rockyou.txt atau buatan sendiri

🚀 Menjalankan:
bash
Copy
Edit
python3 zipcracker.py
📥 Input yang Diminta:
text
Copy
Edit
Masukkan path ke file ZIP: protected.zip
Masukkan path ke file wordlist: wordlist.txt
📜 Struktur Kode dan Penjelasan
Fungsi Utama: brute_force_zip(zip_file_path, wordlist_file_path)
Menjalankan proses brute force terhadap file ZIP.

python
Copy
Edit
with zipfile.ZipFile(zip_file_path) as zf:
    with open(wordlist_file_path, 'r') as wordlist:
        for line in wordlist:
            password = line.strip()
            zf.extractall(pwd=password.encode())
Penanganan error:

FileNotFoundError → jika file tidak ada

zipfile.BadZipFile → jika file rusak/bukan ZIP

RuntimeError → jika password salah

Exception umum lainnya → untuk error tidak terduga

Fungsi main()
Membaca input dari user dan memanggil fungsi brute force.

python
Copy
Edit
zip_file_path = input('Masukkan path ke file ZIP: ')
wordlist_file_path = input('Masukkan path ke file wordlist: ')
📌 Catatan Penting
❗ Tool ini hanya untuk pembelajaran atau pengujian keamanan pribadi.

🚫 Jangan digunakan untuk akses tanpa izin (unauthorized access).

⚡ Disarankan menggunakan wordlist ringan untuk testing awal.

🔄 Rencana Pengembangan Selanjutnya
Tools ini dapat dikembangkan lebih lanjut menjadi modular:

📂 Tambahkan dukungan untuk file RAR (rarfile module)

📄 Tambahkan dukungan untuk file PDF (PyPDF2 atau pikepdf)

🔑 Integrasi GUI sederhana (misalnya Tkinter atau CustomTkinter)

🌐 Web interface dengan Flask untuk demo online

