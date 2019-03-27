''' Nama  : Tika pratiwi
    NIM   : L200170046
    Kelas : B
'''
class MhsTIF(object):
    def __init__(self, nama, umur, kota, us):
        self.nama = nama
        self.umur = umur
        self.kotaTinggal = kota
        self.uangSaku = us

    def __str__(self):
        x = self.nama + ', umur' + str(self.umur) \
            + '. Tinggal di ' + self.kotaTinggal \
            + '. Uang saku ' + str(self.uangSaku) \
            + 'tiap bulannya.'
        return x

    def ambilNama(self):
        return self.nama
    def ambilUmur(self):
        return self.umur
    def ambilKota(self):
        return self.kotaTinggal
    def ambilUangSaku(self):
        return self.uangSaku

m0 = MhsTIF('Tika pratiwi', 13, 'Magetan', 250000)
m1 = MhsTIF('Ika', 12, 'Sukoharjo', 240000)
m2 = MhsTIF('Ahmad', 20, 'Surakarta', 250000)
m3 = MhsTIF('Chandra', 18, 'Surakarta', 235000)
m4 = MhsTIF('Eka', 14, 'Boyolali', 240000)
m5 = MhsTIF('Fandi', 31, 'Salatiga', 250000)
m6 = MhsTIF('Deni', 13, 'Klaten', 245000)
m7 = MhsTIF('Galuh', 15, 'Wonogiri', 245000)
m8 = MhsTIF('Janto', 23, 'Klaten', 245000)
m9 = MhsTIF('Hasan', 24, 'Karanganyar', 270000)
m10 = MhsTIF('Khalid', 29, 'Purwodadi', 265000)
m11 = MhsTIF('Budi', 41, 'Klaten', 210000)

Daftar = [m0, m1, m2, m3, m4, m5, m6, m7, m8, m9, m10, m11]

def cariKota(target):
    y = []
    for i in Daftar:
        if i.kotaTinggal == target:
            hasil = Daftar.index(i)
            y.append(hasil)
    return y
#No2
def cariTerkecil(Daftar):
    n = len(Daftar)
    #Anggap item pertama adalah yang terkecil
    terkecil = Daftar[0]
    #tentukan apakah item lain lebih kecil
    for i in range(1,n):
        if Daftar[i].uangSaku < terkecil.uangSaku:
            terkecil = Daftar[i]

    return terkecil

#No3
def cariTerkecil(Daftar):
    n = len(Daftar)
    #Anggap item pertama adalah yang terkecil
    terkecil = [Daftar[0]]
    #tentukan apakah item lain lebih kecil
    for i in range(1,n):
        if Daftar[i].uangSaku < terkecil[0].uangSaku:
            terkecil = [Daftar[i]]
        elif Daftar[i].uangSaku == terkecil[0].uangSaku:
            terkecil.append(Daftar[i])
    return terkecil

#No4
def cariDaftarUangSakuKurang(kumpulan):
    b = []  
    for i in kumpulan:
        if i.uangSaku < 250000:
            terkecil = i.uangSaku
            b.append(kumpulan.index(i))
    return b
