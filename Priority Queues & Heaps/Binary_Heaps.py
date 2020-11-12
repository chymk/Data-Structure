class Heap:
    def __init__(self):
        self.heapList = [0]
        self.size = 0

    def parent(self,index):
        # node at ith Location it's parent will be at i-1/2 location
        return index/2

    def leftChild(self,index):
        return 2*index+1

    def rightChild(self,index):
        return 2*index+1

    def getMaximum(self):
        if self.size == 0:
            return -1
        return self.heapList[0]

    def getMinimum(self):
        if self.size == 0:
            return -1
        return self.heapList[0]

    def percolateDown(self,i):
        while (i*2) <= self.size:
            minimumChild = self.minChild(i)
            if self.heapList[i] > self.heapList[minimumChild]:
                tmp = self.heapList[i]
                self.heapList[i] = self.heapList[minimumChild]
                self.heapList[minimumChild] = tmp
            i = minimumChild

    def minChild(self,i):
        if i*2+1 > self.size:
            return i*2
        else:
            if self.heapList[i*2] < self.heapList[i*2+1]:
                return i*2
            else:
                return i*2+1


    def percolateUp(self,i):
        while i//2>0:
            if self.heapList[i] < self.heapList[i//2]:
                tmp = self.heapList[i//2]
                self.heapList[i//2] = self.heapList[i]
                self.heapList[i] = tmp
            i = i//2


    def deleteMax(self):
        revival = self.heapList[1]
        self.heapList[1] = self.heapList[self.size]
        self.size = self.size-1
        self.heapList.pop()
        self.percolateDown(1)
        return revival

    def deleteMin(self):
        revival = self.heapList[1]
        self.heapList[1] = self.heapList[self.size]
        self.size = self.size-1
        self.heapList.pop()
        self.percolateDown(1)
        return revival

    def insert(self,k):
        self.heapList.append(k)
        self.size = self.size +1
        self.percolateUp(self.size)


    def buildHeap(self,A):
        i = len(A)//2
        self.size = len(A)
        self.heapList = [0]+A[:]
        while i>0:
            self.percolateDown(i)
            i = i-1


