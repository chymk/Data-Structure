def reverseLinkedListInPair(self):
    current = self.head
    while current is not None and current.next is not None:
        if current.data != current.next.data:
            self.swapData(self,current.data,current.next.data)
        current = current.next.next
    return

def swapData(self,a,b):
    temp = a.data
    a.data = b.data
    b.data = temp
    return
