class PriorityQueue(object):
    def __init__(self):
        self.qlist = []
    def __len__(self):
        return len(self.qlist)
    def is_empty(self):
        return len(self) == 0
    def enqueue(self, data, priority):
        entry = _PriorityQEntry(data, priority)
        self.qlist.append(entry)
    def dequeue(self):
        A = []
        for i in self.qlist:
            A.append(i)
        s = 0
        for i in range(1, len(self.qlist)):
            if A[i].priority < A[s].priority:
                s = i
        hasil = self.qlist.pop(s)
        return hasil.item

class _PriorityQEntry():
    def __init__(self, data, priority):
        self.item = data
        self.priority = priority
        
S = PriorityQueue()
S.enqueue("merah", 21)
S.enqueue("hijau", 5)
S.enqueue("biru", 10)
S.enqueue("hitam", 12)
S.enqueue("putih", 13)
print (S.dequeue())
print (S.dequeue())
print (S.dequeue())
print (S.dequeue())
print (S.dequeue())

