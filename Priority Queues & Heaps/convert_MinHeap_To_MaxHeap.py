class Convert:
    def __init__(self):
        self.heap = []

    def Left(self, i):
        return 2 * i + 1

    def Right(self, i):
        return 2 * i + 2

    def heapify(self, i):
        largest = i
        left = self.Left(i)
        right = self.Right(i)
        size = len(self.heap)
        if left < size and self.heap[left] > self.heap[i]:
            largest = left
        if right < size and self.heap[right] > self.heap[largest]:
            largest = right
        if largest != i:
            self.heap[largest], self.heap[i] = self.heap[i], self.heap[largest]
            self.heapify(largest)

    def convertMinToMax(self):
        i = (len(self.heap) - 2) // 2
        while i >= 0:
            self.heapify(i)
            i -= 1


h = Convert()
h.heap = [-2, 1, 5, 9, 4, 6, 7]
print(h.heap)
h.convertMinToMax()
print(h.heap)
