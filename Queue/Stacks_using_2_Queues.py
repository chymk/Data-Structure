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
            temp = self.rear.data
            self.front = self.rear = None
            return temp
        else:
            temp = self.front
            self.front = temp.next
            return temp.data


class Stacks:
    def __init__(self):
        self.Q1 = Queue()
        self.Q2 = Queue()

    def push(self,item):
        if  not self.Q1.isEmpty():
            self.Q2.enqueue(item)
            while not self.Q1.isEmpty():
                self.Q2.enqueue(self.Q1.dequeue())
        else:
            self.Q1.enqueue(item)
            while not self.Q2.isEmpty():
                self.Q1.enqueue(self.Q2.dequeue())

    def pop(self):
        if self.Q1.isEmpty() and self.Q2.isEmpty():
            print("Stack is empty")
            return
        if self.Q1.isEmpty():
            x = self.Q2.dequeue()
            print(x)
            return x
        else:
            x = self.Q1.dequeue()
            print(x)
            return x

s = Stacks()
s.push(1)
s.push(2)
s.push(3)
s.pop()
s.pop()
s.pop()
s.pop()
