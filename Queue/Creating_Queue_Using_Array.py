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
        self.Q[self.rear] = item
        self.size = self.size + 1
        print("{} enqueued to queue".format(item))

    def dequeue(self):
        if self.isEmpty():
            print("Queue is Empty")
            return
        print("{} dequeue from queue".format(self.Q[self.front]))
        self.front = (self.front+1) % self.capacity
        self.size = self.size -1


    def queueFront(self):
        if self.isEmpty():
            print("Queue is Empty")
            return
        print(self.Q[self.front])

    def queueRear(self):
        if self.isEmpty():
            print("Queue is Empty")
            return
        print(self.Q[self.rear])

if __name__ == "__main__":
    queue = Queue(30)
    queue.Enqueue(10)
    queue.Enqueue(20)
    queue.Enqueue(30)
    queue.Enqueue(40)
    queue.dequeue()
    queue.queueFront()
    queue.queueRear()

