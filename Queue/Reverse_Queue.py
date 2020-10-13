class Node:
    def __init__(self,data=None):
        self.data = data
        self.next = None

class Queue:
    def __init__(self):
        self.front = self.rear = None

    def isEmpty(self):
        return True if self.front is None else False

    def front(self):
        return -9999 if self.front is None else self.front.data

    def rear(self):
        return -9999 if self.rear is None else self.rear.data

    def enqueue(self,item):
        newNode = Node(item)
        if self.rear is None:
            self.rear = self.front = newNode
            return
        self.rear.next = newNode
        self.rear = newNode

    def dequeue(self):
        if self.isEmpty():
            print("Queue is Empty")
            return
        if self.rear == self.front:
            self.front = self.rear = None
        else:
            temp = self.front
            self.front = temp.next

def displayNode(q):
    if q.isEmpty():
        print("Q is Empty")
        return
    temp = q.front
    while temp is not None:
        print(temp.data,end=" ")
        temp = temp.next
    print("")

def Reverse(q):
    if q.front == q.rear:
        return
    Next = None
    prev = None
    current = q.front
    q.rear = current
    while current is not None:
        Next = current.next
        current.next = prev
        prev = current
        current = Next
    q.front = prev
    return q




q= Queue()
q.enqueue(1)
q.enqueue(2)
q.enqueue(3)
q.enqueue(4)

displayNode(q)
q = Reverse(q)

displayNode(q)


