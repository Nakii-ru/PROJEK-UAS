class View:
    def tampilkan_menu(self):
        print("\nDAFTAR NILAI SISWA")
        print("1.Tambah Data")
        print("2.Lihat Data")
        print("3.Keluar")

    def input_nilai(self):
        nama = input("masukkan nama: ")
        while True:
            try:
                nilai = float(input("masukkan nilai: "))
                if 0 <= nilai <= 100:
                    break
                else:
                    print("nilai harus diantara 0 dan 100")
            except ValueError:
                print("input tidak valid")
        return nama, nilai
    
    def tampilkan_siswa(self, siswa):
        if not siswa:
            print("belum ada data")
        else:
            print("\nDaftar Nilai Siswa")
            print("Nama\t\tNilai")
            print("=" *27)
            for data in siswa:
                print(f"{data['nama']}\t\t{data['nilai']}")