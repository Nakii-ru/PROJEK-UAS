# PROJEK-UAS

NAMA : RIDHO FHADLY HAMZAH

NIM : 312410486

KELAS : TI.24.A5

# Hasil Eksekusi Program
![prak.pict](https://github.com/Nakii-ru/prak.pict/blob/main/Screenshot%202025-01-08%20022226.png?raw=true)
![prak.pict](https://github.com/Nakii-ru/prak.pict/blob/main/Screenshot%202025-01-08%20022249.png?raw=true)

# Penjelasan
# File data.py
`Class: Data`

Class ini bertanggung jawab untuk menyimpan dan mengelola data siswa, seperti nama dan nilai
```python
class Data:
    def __init__(self):
        self.siswa = []
```
  `__init__` Method
  
  Fungsi: Menginisialisasi atribut siswa, yang berupa list kosong, yang nantinya akan digunakan untuk menyimpan data siswa dalam bentuk `dictionary` (berisi nama dan nilai).

  Penjelasan: Saat objek dari class `Data` dibuat, atribut `siswa` akan selalu dimulai dengan list kosong.
```python
    def tambah_nilai(self,nama,nilai):
        self.siswa.append({"nama": nama, "nilai": nilai})
```
`tambah_nilai` Method

Fungsi: Menambahkan data siswa yang terdiri dari nama dan nilai ke dalam list siswa.
        
Penjelasan: Method ini akan menambahkan dictionary berisi nama dan nilai ke dalam list siswa.
```python
    def get_siswa(self):
        return self.siswa
```
get_siswa Method

Fungsi: Mengambil dan mengembalikan seluruh data siswa yang sudah disimpan dalam atribut siswa.
        
Penjelasan: Fungsi ini digunakan untuk mengambil data yang sudah dimasukkan dan memudahkan kita untuk melihat semua data siswa.

# File view.py
`Class: View`

Class ini bertanggung jawab untuk menangani input dan output, serta interaksi dengan pengguna.
```python
class View:
    def tampilkan_menu(self):
        print("\nDAFTAR NILAI SISWA")
        print("1.Tambah Data")
        print("2.Lihat Data")
        print("3.Keluar")
```
`tampilkan_menu` Method

Fungsi: Menampilkan menu utama kepada pengguna yang berisi tiga opsi:(1)Menambah nilai siswa,(2)Melihat daftar nilai siswa,(3)Keluar dari program.

Penjelasan: Menu ini akan ditampilkan setiap kali program dijalankan, memungkinkan pengguna untuk memilih tindakan yang diinginkan.
```python
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
```
`input_nilai` Method

  Fungsi: Menerima input nama siswa dan nilai dari pengguna.
    
  Proses Validasi: Program akan meminta nama siswa dan memastikan nilai yang dimasukkan adalah angka antara 0 hingga 100.
  
  Jika input tidak valid (bukan angka atau tidak dalam rentang 0-100), pengguna akan diminta untuk mencoba lagi.
  
  Penjelasan: Fungsi ini memastikan bahwa data yang dimasukkan oleh pengguna sesuai dengan format yang diharapkan.
```python
    def tampilkan_siswa(self, siswa):
        if not siswa:
            print("belum ada data")
        else:
            print("\nDaftar Nilai Siswa")
            print("=" *25)
            print("Nama\t\tNilai")
            print("=" *25)
            for data in siswa:
                print(f"{data['nama']}\t\t{data['nilai']}")
            print("=" *25)
```
`tampilkan_siswa` Method

Fungsi: Menampilkan daftar nama dan nilai siswa.

Penjelasan: Jika tidak ada data siswa, maka akan muncul pesan "Belum ada data nilai siswa". Jika ada, akan ditampilkan nama dan nilai siswa dalam format tabel.

# File `process.py`
Class: Process

Class ini mengelola alur program dengan menghubungkan antara View dan Data
```python
from data import Data
from view import View

class Process:
    def __init__(self):
        self.data = Data()
        self.view = View()
```
`__init__` Method

Fungsi: Menginisialisasi objek Data dan View untuk dipakai dalam proses program.

Penjelasan: Dalam method ini, objek data dibuat sebagai instance dari class Data, dan objek view dibuat sebagai instance dari class View.
```python
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
```
run Method

Fungsi: Mengontrol alur utama program dengan menampilkan menu dan menangani input pengguna.
    
Proses:
        
Program akan terus menampilkan menu hingga pengguna memilih opsi untuk keluar.
        
Jika pengguna memilih opsi 1, maka program akan meminta input nilai siswa dan menyimpannya ke dalam data.

Jika memilih opsi 2, program akan menampilkan daftar nilai siswa.

Jika memilih opsi 3, program akan berhenti dan mengucapkan terima kasih.

Jika input tidak valid, pengguna akan diminta untuk memilih opsi yang benar.

Penjelasan: Method ini menjaga agar program berjalan sesuai dengan alur yang diinginkan oleh pengguna.

## File `main.py`
Pemeriksaan if __name__ == "__main__":
```python
from process import Process

if __name__ == "__main__":
    Process().run()
```
Fungsi: Untuk memastikan bahwa file ini dijalankan langsung sebagai program utama, bukan diimpor sebagai modul.

Proses: Jika file ini dijalankan langsung, objek dari class Process akan dibuat, dan method run akan dipanggil untuk menjalankan program.
