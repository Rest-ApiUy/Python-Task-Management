# fungsi.py
"""
Modul untuk operasi-operasi manajemen tugas
Memiliki fungsi-fungsi main untuk mengelola tugas
"""

from datetime import datetime

# Variabel global untuk menyimpan daftar tugas
daftar_tugas = []

def tambah_tugas(judul, deskripsi=""):
    """
    Menambah tugas baru ke dalam daftar
    Parameter by value: judul dan deskripsi disalin nilainya
    """
    tugas_baru = {
        'id': len(daftar_tugas) + 1,
        'judul': judul,
        'deskripsi': deskripsi,
        'status': 'belum selesai',
        'tanggal_dibuat': datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    }
    daftar_tugas.append(tugas_baru)  # Parameter by reference: mengubah list global
    print(f"Tugas '{judul}' berhasil ditambahkan!")

def tampilkan_tugas():
    """
    Menampilkan semua tugas dalam daftar
    Menggunakan fungsi bawaan Python: len(), enumerate()
    """
    if not daftar_tugas:
        print("Tidak ada tugas dalam daftar.")
        return
    
    print("\n" + "="*60)
    print("DAFTAR TUGAS")
    print("="*60)
    
    for indeks, tugas in enumerate(daftar_tugas, 1):  # Fungsi bawaan enumerate()
        status_simbol = "[SELESAI]" if tugas['status'] == 'selesai' else "[PENDING]"
        print(f"{status_simbol} [{tugas['id']}] {tugas['judul']}")
        if tugas['deskripsi']:
            print(f"    Deskripsi: {tugas['deskripsi']}")
        print(f"    Dibuat: {tugas['tanggal_dibuat']}")
        print("-" * 40)

def tandai_selesai(id_tugas):
    """
    Menandai tugas sebagai selesai berdasarkan ID
    Parameter by value: id_tugas
    Parameter by reference: mengubah daftar_tugas global
    """
    for tugas in daftar_tugas:
        if tugas['id'] == id_tugas:
            tugas['status'] = 'selesai'
            tugas['tanggal_selesai'] = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            print(f"Tugas '{tugas['judul']}' telah ditandai sebagai selesai!")
            return True
    
    print(f"Tugas dengan ID {id_tugas} tidak ditemukan.")
    return False

def hapus_tugas(id_tugas):
    """
    Menghapus tugas berdasarkan ID
    Parameter by value: id_tugas
    Parameter by reference: mengubah daftar_tugas global
    """
    global daftar_tugas
    
    for i, tugas in enumerate(daftar_tugas):
        if tugas['id'] == id_tugas:
            tugas_terhapus = daftar_tugas.pop(i)  # Fungsi bawaan pop()
            # Update ID untuk tugas-tugas setelahnya
            for j in range(i, len(daftar_tugas)):
                daftar_tugas[j]['id'] = j + 1
            print(f"Tugas '{tugas_terhapus['judul']}' telah dihapus!")
            return True
    
    print(f"Tugas dengan ID {id_tugas} tidak ditemukan.")
    return False

def pencarian_rekursif(list_tugas, kata_kunci, indeks=0, tugas_ditemukan=None):
    """
    FUNGSI REKURSIF untuk mencari tugas berdasarkan kata kunci
    Parameter by value: kata_kunci, indeks
    Parameter by reference: list_tugas, tugas_ditemukan (list yang diubah)
    """
    if tugas_ditemukan is None:
        tugas_ditemukan = []
    
    # Base case: jika sudah mencapai akhir list
    if indeks >= len(list_tugas):
        return tugas_ditemukan
    
    # Cek apakah kata_kunci ada dalam judul atau deskripsi
    tugas_sekarang = list_tugas[indeks]
    kata_kunci_kecil = kata_kunci.lower()
    
    if (kata_kunci_kecil in tugas_sekarang['judul'].lower() or 
        kata_kunci_kecil in tugas_sekarang['deskripsi'].lower()):
        tugas_ditemukan.append(tugas_sekarang)
    
    # Recursive case: lanjut ke tugas berikutnya
    return pencarian_rekursif(list_tugas, kata_kunci, indeks + 1, tugas_ditemukan)

def cari_tugas(kata_kunci):
    """
    Wrapper function untuk pencarian rekursif
    Menggunakan fungsi rekursif pencarian_rekursif()
    """
    if not kata_kunci.strip():  # Fungsi bawaan strip()
        print("Kata kunci tidak boleh kosong!")
        return
    
    tugas_ditemukan = pencarian_rekursif(daftar_tugas, kata_kunci)
    
    if not tugas_ditemukan:
        print(f"Tidak ditemukan tugas dengan kata kunci '{kata_kunci}'")
        return
    
    print(f"\nHASIL PENCARIAN untuk '{kata_kunci}':")
    print("="*50)
    for tugas in tugas_ditemukan:
        status_simbol = "[SELESAI]" if tugas['status'] == 'selesai' else "[PENDING]"
        print(f"{status_simbol} [{tugas['id']}] {tugas['judul']}")
        if tugas['deskripsi']:
            print(f"    Deskripsi: {tugas['deskripsi']}")
        print("-" * 30)

def tampilkan_statistik():
    """
    Menampilkan statistik tugas
    Menggunakan fungsi bawaan: len(), sum(), filter()
    """
    total_tugas = len(daftar_tugas)  # Fungsi bawaan len()
    
    # Menggunakan filter() dan len() untuk menghitung tugas selesai
    tugas_selesai = len(list(filter(lambda x: x['status'] == 'selesai', daftar_tugas)))
    tugas_pending = total_tugas - tugas_selesai
    
    print("\n" + "="*40)
    print("STATISTIK TUGAS")
    print("="*40)
    print(f"Total Tugas     : {total_tugas}")
    print(f"Selesai         : {tugas_selesai}")
    print(f"Belum Selesai   : {tugas_pending}")
    
    if total_tugas > 0:
        tingkat_selesai = (tugas_selesai / total_tugas) * 100
        print(f"Tingkat Selesai : {tingkat_selesai:.1f}%")
    print("="*40)

def hitung_tugas():
    """
    Mengembalikan jumlah total tugas
    Fungsi utility yang menggunakan variabel global
    """
    return len(daftar_tugas)

def hapus_semua_tugas():
    """
    Menghapus semua tugas (untuk testing)
    Parameter by reference: mengubah daftar_tugas global
    """
    global daftar_tugas
    daftar_tugas.clear()  # Fungsi bawaan clear()
    print("Semua tugas telah dihapus!")

