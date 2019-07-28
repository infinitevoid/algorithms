

def _left(i):
    return 2*i + 1
def _right(i):
    return 2*i + 2
def _parent(i):
    return i//2
def _swap(array, i, j):
    array[i],array[j] = array[j],array[i]

class MinHeap:
    def __init__(self, capacity):
        self.data = [None for i in range(capacity)]
        self.capacity = capacity
        self.size = 0
    def insert(self, elem):
        ind = self.size
        self.data[ind] = elem
        self.size += 1
        while self.data[_parent(ind)] > self.data[ind]:
            _swap(self.data, _parent(ind), ind)
            ind = _parent(ind)
    def heapify(self, ind: int):
        smallest = ind
        left = _left(ind)
        right = _right(ind)
        if left < self.size and self.data[left] < self.data[smallest]:
            smallest = left
        if right < self.size and self.data[right] < self.data[smallest]:
            smallest = right
        if ind != smallest:
            _swap(self.data, smallest, ind)
            self.heapify(smallest)
    def extract_min(self):
        self.size -= 1
        temp = self.data[0]
        self.data[0] = self.data[self.size]
        self.data[self.size] = 0
        self.heapify(0)
        return temp
    def pop(self):
        return self.extract_min()
    def __len__(self):
        return self.size
    def get_min(self):
        return self.data[0]

"""
###Test###
if __name__ == "__main__":
    import random
    h = MinHeap(20)
    for i in range(20):
        h.insert(random.randint(-100,100))
    print(h.data)
    print(h.get_min(),h.extract_min())
    print(h.data)
"""
