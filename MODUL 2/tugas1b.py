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
    def hitungKonsonan(self, string):
        self.vok = 0
        self.x = "aiueoAIUEO"
        for car in string.lower():
            if car not in self.x:
                self.vok += 1
        self.vocal= len (string)
        return (self.vocal, self.vok)
        
