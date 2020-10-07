def checkEvenOdd(self):
    current = self.head
    if current is None:
        print("LinkedList Empty")
    while current is not None and current.next is not None:
        current = current.next.next
    if current is None or current.next is not None:
        print("Linkedlist is Even")
    else:
        print("LinkedList is Odd")
