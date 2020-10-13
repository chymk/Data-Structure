class Node:
    def __init__(self,data = None):
        self.data = data
        self.next = None

class CircularQueue:
    def __init__(self):
        self.front = None
        self.rear = None

    def enqueue(self,item):
        newNode = Node(item)
        if self.front is None:
            self.front = newNode
        else:
            self.rear.next = newNode
        self.rear = newNode
        self.rear.next = self.front


    def dequeue(self):
        if self.front is None:
            print("Queue is Empty")
            return
        if self.front == self.rear:
            temp = self.q.front.data
            self.rear = None
            self.front = None

        else:
            temp = self.front
            self.front = temp.next
            self.rear.next = self.front
            print(temp.data)
            return temp.data


def displayQueue(q):
    if q.front is None:
        print("Queue is Empty")
        return
    temp = q.front
    while temp.next != q.front:
        print(temp.data,end=" ")
        temp = temp.next
    print(temp.data, end=" ")
    print("")

q= CircularQueue()
q.enqueue(1)
q.enqueue(2)
q.enqueue(3)
q.enqueue(4)
q.enqueue(5)
q.enqueue(6)


displayQueue(q)

q.dequeue()
q.dequeue()
displayQueue(q)