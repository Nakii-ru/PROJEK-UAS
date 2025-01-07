from data import Data
from view import View

class Process:
    def __init__(self):
        self.data = Data()
        self.view = View()

    def run(self):
        while True:
            self.view.tampilkan_menu()
            pilihan = input("Pilih Opsi (1-3): ")

            if pilihan == "1":
                nilai = self.view.input_nilai()
                if nilai:
                    nama, nilai_akhhir = nilai
                    self.data.tambah_nilai(nama, nilai_akhhir)
                    print("Data berhasil ditambahkan")

            elif pilihan == "2":
                siswa = self.data.get_siswa()
                self.view.tampilkan_siswa(siswa)

            elif pilihan == "3":
                print("Berhasil keluar dari program!")
                break

            else:
                print("Pilihan tidak valid. Coba lagi")