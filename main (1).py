import backend 
import logger

def tampilkan_menu(): 
    print("\n=== APLIKASI DAFTAR BELANJA ===") 
    print("1. Tambah item") 
    print("2. Lihat semua item") 
    print("3. Hapus item") 
    print("4. Edit item") 
    print("5. Cari item") 
    print("6. Saran bahan (API)") 
    print("7. Keluar")

def main(): 
    logger.tulis_log("Program dimulai")
    while True: 
        tampilkan_menu() 
        pilihan = input("Pilih menu (1-7): ")

        if pilihan == '1':
            item = input("Nama item: ")
            if item.strip() == "":
                print(" Nama item tidak boleh kosong.")
                logger.tulis_log("Peringatan: input item kosong")
            else:
                pesan = backend.tambah_item(item)
                print(pesan)
                logger.tulis_log(f"Menambah item: {item}")

        elif pilihan == '2':
            daftar = backend.semua_item()
            if not daftar:
                print(" Daftar belanja kosong.")
                logger.tulis_log("Melihat daftar (kosong)")
            else:
                print("\n Daftar Belanja:")
                for i, nama in enumerate(daftar, start=1):
                    print(f"   {i}. {nama}")
                logger.tulis_log("Melihat daftar item")

        elif pilihan == '3':
            daftar = backend.semua_item()
            if not daftar:
                print(" Tidak ada item untuk dihapus.")
                logger.tulis_log("Mencoba hapus saat kosong")
                continue
            for i, nama in enumerate(daftar, start=1):
                print(f"   {i}. {nama}")
            try:
                no = int(input("Nomor item yang akan dihapus: "))
                pesan = backend.hapus_item(no)
                print(pesan)
                logger.tulis_log(f"Menghapus item nomor {no}")
            except ValueError:
                print(" Masukkan angka.")
                logger.tulis_log("Error: input hapus bukan angka")

        elif pilihan == '4':
            daftar = backend.semua_item()
            if not daftar:
                print(" Tidak ada item untuk diedit.")
                logger.tulis_log("Mencoba edit saat kosong")
                continue
            for i, nama in enumerate(daftar, start=1):
                print(f"   {i}. {nama}")
            try:
                no = int(input("Nomor item yang akan diedit: "))
                nama_baru = input("Nama baru: ")
                if nama_baru.strip() == "":
                    print(" Nama baru tidak boleh kosong.")
                    logger.tulis_log("Peringatan: input edit kosong")
                else:
                    pesan = backend.edit_item(no, nama_baru)
                    print(pesan)
                    logger.tulis_log(f"Edit item nomor {no} menjadi {nama_baru}")
            except ValueError:
                print(" Masukkan angka.")
                logger.tulis_log("Error: input edit bukan angka")

        elif pilihan == '5':
            kata = input("Masukkan kata kunci: ")
            if kata.strip() == "":
                print(" Kata kunci tidak boleh kosong.")
                logger.tulis_log("Peringatan: pencarian kosong")
            else:
                hasil = backend.cari_item(kata)
                if not hasil:
                    print(" Tidak ada item yang cocok.")
                    logger.tulis_log(f"Pencarian '{kata}' tidak ditemukan")
                else:
                    print("\n Hasil Pencarian:")
                    for i, item in enumerate(hasil, start=1):
                        print(f"   {i}. {item}")
                    logger.tulis_log(f"Pencarian '{kata}' menemukan {len(hasil)} item")

        elif pilihan == '6':
            print("\n Mengambil saran bahan dari internet...")
            logger.tulis_log("Memanggil API saran bahan")
            saran = backend.saran_bahan()
            if not saran or " Gagal" in saran[0]:
                print(saran[0])
                logger.tulis_log("Gagal mengambil saran dari API")
            else:
                print("\n Saran Bahan (dari API):")
                for i, item in enumerate(saran, start=1):
                    print(f"   {i}. {item}")
                logger.tulis_log("Berhasil mengambil saran dari API")

        elif pilihan == '7':
            print(" Sampai jumpa!")
            logger.tulis_log("Program selesai")
            break

        else:
            print( " Pilihan tidak valid.")
            logger.tulis_log(f"Pilihan tidak valid: {pilihan}")
        
if __name__ == "__main__": 
    main()