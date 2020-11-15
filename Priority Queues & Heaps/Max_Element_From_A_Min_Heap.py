def findMaxInMinHeap(self):
    Max = 0
    for i in range ((self.size+1)//2,self.size):
        Max = max(Max,self.array[i])
        return Max