def delete(self,i):
    if i<self.size:
        print("Location Outbound")
        return

    key = self.array[i]
    self.array[i] = self.array[self.size-1]
    self.size = self.size-1
    self.percolateDown(i)
    return key

