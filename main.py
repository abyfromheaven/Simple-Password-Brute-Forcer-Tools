import zipfile
import sys

def brute_force_zip(zip_file_path, wordlist_file_path):
    try:
        with zipfile.ZipFile(zip_file_path) as zf:
            with open(wordlist_file_path, 'r', encoding='utf-8', errors='ignore') as wordlist:
                for line in wordlist:
                    password = line.strip()
                    if not password:
                        continue
                    try:
                        # Mencoba untuk mengekstrak dengan kata sandi
                        zf.extractall(pwd=password.encode())
                        print(f'[+] Kata sandi ditemukan: {password}')
                        return True
                    except (RuntimeError, zipfile.BadZipFile):
                        # Kata sandi salah atau file rusak
                        print(f'[-] Mencoba kata sandi: {password} - salah')
                        continue
                print('[-] Kata sandi tidak ditemukan dalam wordlist.')
                return False
    except FileNotFoundError as e:
        print(f'[!] File tidak ditemukan: {e.filename}')
        return False
    except zipfile.BadZipFile:
        print('[!] File ZIP rusak atau bukan file ZIP.')
        return False
    except Exception as e:
        print(f'[!] Terjadi kesalahan yang tidak terduga: {e}')
        return False

def main():
    print('=== Alat Brute Force Kata Sandi ZIP ===')
    zip_file_path = input('Masukkan path ke file ZIP: ').strip()
    wordlist_file_path = input('Masukkan path ke file wordlist: ').strip()
    print(f'Mulai brute force pada "{zip_file_path}" menggunakan wordlist "{wordlist_file_path}"...')
    
    success = brute_force_zip(zip_file_path, wordlist_file_path)
    if not success:
        sys.exit(1)
    else:
        print('Selesai.')

if __name__ == '__main__':
    main()

