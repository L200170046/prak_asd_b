class Pesan(object):
    """
        Sebuah class bernama pesan.
    """
    def __init__(self, sebuahString):
        self.teks = sebuahString
    def cetakIni(self):
        print(self.teks)
    def cetakPakaiHurufKapital(self):
        print(str.upper(self.teks))
    def cetakPakaiHurufKecil(self):
        print(str.lower(self.teks))
    def jumKar(self):
        return len(self.teks)
    def cetajJumlahKarakterku(self):
        print('Kalimatku mempunya', len(self.teks), 'karakter')
    def perbarui(self, stringBaru):
        self.teks = stringBaru
    def apakahTErkandung(self, sebuahSting):
        if sebuahString == 'ege':
            return True
        elif sebuahString =='eka':
            return False
        else:
            return 'Bukan kalimat'
