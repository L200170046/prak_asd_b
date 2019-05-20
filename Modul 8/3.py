class stack():
    def __init__(self): #membuat stack kosong
        self.item = []
    def empty(self): #mengembalikan nilai boolean yg menunjukkan apakah
                     #stack itu kosong
        return len(self) == 0
    def __len__(self): #mengembalikan byknya item di stack
        return len(self.item)
    def peek(self): #mengembalikan nilai posisi atas tnpa menghapus data dan
                    #mengembalikan nilai dr item yg paling atas tnp mnghpus
        assert not self.empty()
        return self.item[-1]
    def pop(self): #mengembalikan nilai posisi atas lalu menghapus, stack
                   #kosong tdk dpt kosong
        assert not self.empty()
        return self.item.pop()
    def push(self, data): #mendorong item ke stact. menambah item ke puncak
                          #stack
        self.item.append(data)


nilai = stack()  #menyimpan kelas stack pada variable nilai
for i in range(16): #range sampai 15
    if i % 3 == 0: #jika i habis dibagi 3 adalah 0
        nilai.push(i) #akan memasukkan data pada variable nilai
    elif i % 4 == 0 : #jika i habis dibagi 4 adalah 0
        nilai.pop() #akan mengambil data yang paling atas pada variable nilai

print(nilai.item) #menampilkan item pada nilai
