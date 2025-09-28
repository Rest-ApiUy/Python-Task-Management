import os
import sys

# Import semua fungsi dari modul fungsi
from fungsi import (
    tambah_tugas, tampilkan_tugas, tandai_selesai, hapus_tugas, 
    cari_tugas, tampilkan_statistik, hitung_tugas, daftar_tugas
)

def bersihkan_layar():
    """
    Membersihkan layar terminal
    Menggunakan fungsi bawaan os.system()
    """
    os.system('cls' if os.name == 'nt' else 'clear')

def tampilkan_menu():
    """
    Menampilkan menu main aplikasi
    """
    print("\n" + "="*50)
    print("SISTEM MANAJEMEN TUGAS SEDERHANA")
    print("="*50)
    print("1. Tambah Tugas Baru")
    print("2. Tampilkan Daftar Tugas")
    print("3. Tandai Tugas Selesai")
    print("4. Hapus Tugas")
    print("5. Cari Tugas")
    print("6. Tampilkan Statistik")
    print("7. Refresh Layar")
    print("0. Keluar")
    print("="*50)
    print(f"Saat ini ada {hitung_tugas()} tugas dalam sistem")

def ambil_input_angka(prompt):
    """
    Mengambil input integer dengan validasi
    Parameter by value: prompt
    Menggunakan fungsi bawaan: int(), input()
    """
    while True:
        try:
            return int(input(prompt))  # Fungsi bawaan int() dan input()
        except ValueError:
            print("Mohon masukkan angka yang valid!")
        except KeyboardInterrupt:
            print("\nProgram dihentikan oleh pengguna.")
            sys.exit(0)

def ambil_input_teks(prompt, wajib=True):
    """
    Mengambil input string dengan validasi
    Parameter by value: prompt, wajib
    Menggunakan fungsi bawaan: input(), strip()
    """
    while True:
        try:
            input_pengguna = input(prompt).strip()  # Fungsi bawaan strip()
            if wajib and not input_pengguna:
                print("Input tidak boleh kosong!")
                continue
            return input_pengguna
        except KeyboardInterrupt:
            print("\nProgram dihentikan oleh pengguna.")
            sys.exit(0)

def proses_tambah_tugas():
    """
    Menangani proses penambahan tugas baru
    Fungsi untuk memisahkan logika menu dari operasi tugas
    """
    print("\nTAMBAH TUGAS BARU")
    print("-" * 30)
    
    judul = ambil_input_teks("Judul tugas: ", wajib=True)
    deskripsi = ambil_input_teks("Deskripsi (opsional, Enter untuk lewati): ", wajib=False)
    
    tambah_tugas(judul, deskripsi)  # Memanggil fungsi dari modul lain

def proses_tandai_selesai():
    """
    Menangani proses menandai tugas sebagai selesai
    """
    if hitung_tugas() == 0:
        print("Tidak ada tugas untuk ditandai sebagai selesai.")
        return
    
    tampilkan_tugas()
    id_tugas = ambil_input_angka("\nMasukkan ID tugas yang selesai: ")
    tandai_selesai(id_tugas)

def proses_hapus_tugas():
    """
    Menangani proses penghapusan tugas
    """
    if hitung_tugas() == 0:
        print("Tidak ada tugas untuk dihapus.")
        return
    
    tampilkan_tugas()
    id_tugas = ambil_input_angka("\nMasukkan ID tugas yang akan dihapus: ")
    
    # Konfirmasi penghapusan
    konfirmasi = ambil_input_teks(f"Yakin ingin menghapus tugas ID {id_tugas}? (y/n): ", wajib=True)
    
    if konfirmasi.lower() in ['y', 'yes', 'ya']:  # Fungsi bawaan lower()
        hapus_tugas(id_tugas)
    else:
        print("Penghapusan dibatalkan.")

def proses_cari_tugas():
    """
    Menangani proses pencarian tugas
    """
    kata_kunci = ambil_input_teks("\nMasukkan kata kunci pencarian: ", wajib=True)
    cari_tugas(kata_kunci)

def main():
    """
    Fungsi main program
    Mengatur alur program dan menangani menu main
    """
    print("Memulai Sistem Manajemen Tugas...")
    print("Tip: Gunakan Ctrl+C untuk keluar kapan saja")
    
    while True:
        try:
            tampilkan_menu()
            pilihan = ambil_input_angka("Pilih menu (0-7): ")
            
            if pilihan == 1:
                proses_tambah_tugas()
                
            elif pilihan == 2:
                tampilkan_tugas()
                
            elif pilihan == 3:
                proses_tandai_selesai()
                
            elif pilihan == 4:
                proses_hapus_tugas()
                
            elif pilihan == 5:
                proses_cari_tugas()
                
            elif pilihan == 6:
                tampilkan_statistik()
                
            elif pilihan == 7:
                bersihkan_layar()
                print("Layar telah direfresh!")
                
            elif pilihan == 0:
                print("\nTerima kasih telah menggunakan Sistem Manajemen Tugas!")
                print(f"Total tugas yang dikelola: {hitung_tugas()}")
                break
                
            else:
                print("Pilihan tidak valid. Silakan pilih 0-7.")
            
            # Pause sebelum kembali ke menu (kecuali untuk refresh dan exit)
            if pilihan not in [7, 0]:
                input("\nTekan Enter untuk kembali ke menu...")
                
        except KeyboardInterrupt:
            print("\n\nProgram dihentikan oleh pengguna. Sampai jumpa!")
            break
        except Exception as e:
            print(f"Terjadi error: {e}")
            print("Program akan kembali ke menu main...")
            input("\nTekan Enter untuk melanjutkan...")

if __name__ == "__main__":
    main()

# ================================================================
# Instruksi untuk menjalankan:
# 
# 1. Simpan kode di atas dalam 2 file terpisah:
#    - fungsi.py (bagian pertama)
#    - main.py (bagian kedua)
#
# 2. Pastikan kedua file berada dalam folder yang sama
#
# 3. Buka terminal/command prompt di folder tersebut
#
# 4. Jalankan perintah: python main.py
#    atau: python3 main.py
#
# ================================================================