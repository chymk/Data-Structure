class MaxHeap:
    def __init__(self):
        self.heap = []

    def parent(self, i):
        return i // 2

    def left(self, i):
        return (2 * i) + 1

    def right(self, i):
        return (2 * i) + 2

    def heapifyUp(self, i):
        Parent = self.parent(i)
        if i and self.heap[Parent] < self.heap[i]:
            self.heap[Parent], self.heap[i] = self.heap[i], self.heap[Parent]
            self.heapifyUp(Parent)

    def heapifyDown(self, i):
        largest = i
        size = len(self.heap)
        Left = self.left(i)
        Right = self.right(i)
        if Left < size and self.heap[Left] > self.heap[i]:
            largest = Left
        if Right < size and self.heap[Right] > self.heap[largest]:
            largest = Right
        if largest != i:
            self.heap[largest], self.heap[i] = self.heap[i], self.heap[largest]
            self.heapifyDown(largest)

    def push(self, num):
        self.heap.append(num)
        self.heapifyUp(len(self.heap) - 1)

    def pop(self):
        if len(self.heap) == 0:
            print("Heap is empty")
            return
        self.heap[0] = self.heap[len(self.heap) - 1]
        self.heapifyDown(0)
        self.heap.pop()

    def printHeap(self):
        print("Heap : ", self.heap)


h = MaxHeap()
h.push(1)
h.push(2)
h.push(-1)
h.push(3)
h.push(-2)
h.printHeap()
h.pop()
h.printHeap()
h.pop()
h.printHeap()



