class Mixer:
    fungsi = []
    __activeFungsi = None
    def __init__ (self, nama_merk, jumlah_tungkai_pengaduk, kecepatan_mixer):
        self.nama_merk = nama_merk
        self.jumlah_tungkai_pengaduk = jumlah_tungkai_pengaduk
        self.kecepatan_mixer = kecepatan_mixer
    def nyalakanMixer(self):
        print('Mixer menyala ', self.nama_merk)

    def matikanMixer(self):
        print('Mixer dimatikan ', self.nama_merk)

    def menambahKecepatan(self):
        self.kecepatan_sekarang = self.kecepatan_sekarang + 3
        print('kecepatan_sekarang ', self.kecepatan_sekarang)

    
    def _scan(self):
        self.__fungsi = ['Mengaduk', 'Mencampur', 'Menguleni']

    def _setFungsi(self):
        self.__activefungsi = self.__fungsi[0]

    def getActiveFungsi(self):
        self.__activefungsi = self.__fungsi[0]
        return self.__activefungsi

    def __add__ (self, other):
        return self.kecepatan_mixer + other.kecepatan_mixer


kecepatan1 = Mixer("Phillips", "2", 2)
kecepatan2 = Mixer("Miyako", "2", 3)
print(kecepatan1 + kecepatan2)

