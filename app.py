import json
from datetime import datetime

def tampilkan_menu():
    print("\n===[ TODOL ]===")
    print("Simple To-Do List app\n")
    print("1. Lihat Daftar Tugas")
    print("2. Tambah Tugas Baru")
    print("3. Tandai Tugas Selesai")
    print("4. Hapus Tugas")
    print("5. Simpan Daftar Tugas ke File")
    print("6. Buka Daftar Tugas dari File")
    print("7. Keluar")

def lihat_tugas(daftar_tugas):
    if not daftar_tugas:
        print("\nDan yap! sekarang tidak ada tugas yang tersedia :D")
    else:
        print("\nDaftar Tugas:")
        for index, tugas in enumerate(daftar_tugas, start=1):
            status = "✓" if tugas["selesai"] else " "
            nama = tugas['nama']
            deadline = tugas.get('deadline', 'Tanpa deadline')
            if deadline != 'Tanpa deadline':
                try:
                    deadline_date = datetime.strptime(deadline, '%Y-%m-%d')
                    hari_ini = datetime.now()
                    if deadline_date < hari_ini and not tugas["selesai"]:
                        nama = f"(!) {nama} (Terlambat)"
                    deadline = deadline_date.strftime('%d/%m/%Y')
                except ValueError:
                    pass
            print(f"{index}. [{status}] {nama} (Deadline: {deadline})")

def tambah_tugas(daftar_tugas):
    nama_tugas = input("\nMasukkan nama tugas baru: ")
    
    while True:
        deadline = input("Masukkan deadline (YYYY-MM-DD) atau kosongkan: ")
        if not deadline:
            deadline = "Tanpa deadline"
            break
        try:
            datetime.strptime(deadline, '%Y-%m-%d')
            break
        except ValueError:
            print("Format tanggal tidak valid. Gunakan format YYYY-MM-DD\nContoh: 2025-07-20.")
    
    daftar_tugas.append({
        "nama": nama_tugas,
        "selesai": False,
        "deadline": deadline
    })
    print(f"Tugas '{nama_tugas}' berhasil ditambahkan!")

def tandai_selesai(daftar_tugas):
    lihat_tugas(daftar_tugas)
    if not daftar_tugas:
        return
    
    try:
        nomor = int(input("\nMasukkan nomor tugas yang selesai: ")) - 1
        if 0 <= nomor < len(daftar_tugas):
            daftar_tugas[nomor]["selesai"] = True
            print(f"Tugas '{daftar_tugas[nomor]['nama']}' telah ditandai selesai!")
        else:
            print("Nomor tugas tidak valid!")
    except ValueError:
        print("Masukkan nomor yang valid!")

def hapus_tugas(daftar_tugas):
    lihat_tugas(daftar_tugas)
    if not daftar_tugas:
        return
    
    try:
        nomor = int(input("\nMasukkan nomor tugas yang akan dihapus: ")) - 1
        if 0 <= nomor < len(daftar_tugas):
            tugas_dihapus = daftar_tugas.pop(nomor)
            print(f"Tugas '{tugas_dihapus['nama']}' telah dihapus!")
        else:
            print("Nomor tugas tidak valid!")
    except ValueError:
        print("Masukkan nomor yang valid!")

def simpan_ke_file(daftar_tugas):
    nama_file = input("\nMasukkan nama file untuk disimpan (contoh: tugas.json): ")
    try:
        with open(nama_file, 'w') as file:
            json.dump(daftar_tugas, file)
        print(f"Daftar tugas berhasil disimpan ke {nama_file}!")
    except Exception as e:
        print(f"Gagal menyimpan file: {e}")

def muat_dari_file():
    nama_file = input("\nMasukkan nama file yang akan dibuka (contoh: tugas.json): ")
    try:
        with open(nama_file, 'r') as file:
            daftar_tugas = json.load(file)
        print(f"Daftar tugas berhasil dimuat dari {nama_file}!")
        return daftar_tugas
    except FileNotFoundError:
        print("File tidak ditemukan!")
    except Exception as e:
        print(f"Gagal memuat file: {e}")
    return None

def main():
    daftar_tugas = []
    
    while True:
        tampilkan_menu()
        pilihan = input("\nPilih menu (1-7): ")
        
        if pilihan == "1":
            lihat_tugas(daftar_tugas)
        elif pilihan == "2":
            tambah_tugas(daftar_tugas)
        elif pilihan == "3":
            tandai_selesai(daftar_tugas)
        elif pilihan == "4":
            hapus_tugas(daftar_tugas)
        elif pilihan == "5":
            simpan_ke_file(daftar_tugas)
        elif pilihan == "6":
            tugas_baru = muat_dari_file()
            if tugas_baru is not None:
                daftar_tugas = tugas_baru
        elif pilihan == "7":
            print("\nTerima kasih telah menggunakan TODOL <3")
            break
        else:
            print("\nPilihan tidak valid. Silakan pilih 1-7.")

if __name__ == "__main__":
    main()
