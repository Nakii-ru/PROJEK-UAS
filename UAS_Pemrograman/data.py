class Data:
    def __init__(self):
        self.siswa = []

    def tambah_nilai(self,nama,nilai):
        self.siswa.append({"nama": nama, "nilai": nilai})

    def get_siswa(self):
        return self.siswa