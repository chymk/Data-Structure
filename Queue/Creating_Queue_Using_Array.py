class Queue:
    def __init__(self,capacity):
        self.front = self.size = 0
        self.rear = capacity - 1
        self.Q = [None]*capacity
        self.capacity = capacity

    def isFull(self):
        self.size == self.capacity

    def isEmpty(self):
        self.size == 0

    def Enqueue(self,item):
        if self.isFull():
            print("Queue is full")
            return
        self.rear = (self.rear+1) % self.capacity






    def dequeue(self):
        return
