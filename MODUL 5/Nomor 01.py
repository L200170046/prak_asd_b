''' Nama  : Tika pratiwi
    NIM   : L200170046
    Kelas : B
'''
class MhsTIF(object):
    def __init__(self, nama, umur, kota, NIM):
        self.nama = nama
        self.umur = umur
        self.kotaTinggal = kota
        self.nim = NIM

    def __str__(self):
        x = self.nim
        return x

    def getnim(self):
        return self.nim

m0 = MhsTIF('Tika pratiwi', 13, 'Magetan','L200180048')
m1 = MhsTIF('Ika', 12, 'Sukoharjo','L200180028')
m2 = MhsTIF('Ahmad', 20, 'Surakarta', 'L200180018')
m3 = MhsTIF('Chandra', 18, 'Surakarta','L200180012')
m4 = MhsTIF('Eka', 14, 'Boyolali','L200180132')
m5 = MhsTIF('Fandi', 31, 'Salatiga','L200180042')
m6 = MhsTIF('Deni', 13, 'Klaten', 'L200180088')
m7 = MhsTIF('Galuh', 15, 'Wonogiri', 'L200180014')
m8 = MhsTIF('Janto', 23, 'Klaten', 'L200180022')
m9 = MhsTIF('Hasan', 24, 'Karanganyar', 'L200180124')
m10 = MhsTIF('Khalid', 29, 'Purwodadi', 'L200180089')
m11 = MhsTIF('Budi', 41, 'Klaten', 'L200180010')

Daftar = [m0, m1, m2, m3, m4, m5, m6, m7, m8, m9, m10, m11]

def insertionSort(A):
    n = len(A)
    for i in range(1, n):
        nilai = A[i]
        pos = i
        while pos > 0 and nilai.nim < A[pos - 1].nim:
            A[pos] = A[pos - 1]
            pos = pos - 1
        A[pos] = nilai

def cetakDaftar(d):
    for i in d:
        print (i)
        
insertionSort(Daftar)
cetakDaftar(Daftar)
