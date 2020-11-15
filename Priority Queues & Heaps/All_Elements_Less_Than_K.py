# import the heap functions from Python library
from heapq import heappop, heappush, heapify



class Minheap:

    def __init__(self):
        self.heap = []

    def parent(self,i):
        return (i-1)/2

    def insertKey(self,k):
        heappush(self.heap,k)

    def decreaseKey(self,i,newval):
        self.heap[i] = newval
        while i!=0 and self.heap[int(self.parent(i))] > self.heap[i]:
            # Swap heap[i] with heap[parent(i)]
            self.heap[i],self.heap[int(self.parent(i))] = self.heap[int(self.parent(i))],self.heap[i]

    def extractMin(self):
        return heappop(self.heap)

    def deleteKey(self,i):
        self.decreaseKey(i,float('-inf'))
        self.extractMin()

    def getMin(self):
        return self.heap[0]

    def elementsLessThan_k_Helper(self, i, k):
        if self.heap[i] == k:
            print(self.heap[i],end=" ")
            return
        elif self.heap[i] < k:
            print(self.heap[i],end=" ")
            if (2*i)+1 <= len(self.heap)-1:
                self.elementsLessThan_k_Helper( (2*i)+1, k)
            if (2*i)+2 <= len(self.heap)-1:
                self.elementsLessThan_k_Helper( (2*i)+2, k)
        return

        return
    def elementsLessThan_K(self,k):
        self.elementsLessThan_k_Helper(0,k)
        return


heapObj = Minheap()
heapObj.insertKey(3)
heapObj.insertKey(2)
heapObj.insertKey(1)
heapObj.insertKey(15)
heapObj.insertKey(5)
heapObj.insertKey(4)
heapObj.insertKey(45)


#print(heapObj.extractMin())
#print(heapObj.getMin())
#heapObj.decreaseKey(2, 1)
#print(heapObj.getMin())
heapObj.elementsLessThan_K(15)