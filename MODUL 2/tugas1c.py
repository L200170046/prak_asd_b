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
    def hitunghurufVokal (self):
        voc = 0
        x = "aiueoAIUEO"
        for car in self.teks.lower():
            if car in x:
                voc += 1
        vokal= len(self.teks)
        return voc   
