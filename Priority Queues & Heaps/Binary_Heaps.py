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
