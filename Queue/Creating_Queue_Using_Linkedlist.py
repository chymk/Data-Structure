class Node:
    def __init__(self,data):
        self.data = data
        self.next = None

class Queue:
    def __init__(self):
        self.front = self.rear = None

    def isEmpty(self):
        return self.rear == None

    def Enque(self,item):
        newNode = Node(item)
        if self.rear is None:
            self.rear = self.front = newNode
            return
        self.rear.next = newNode
        self.rear = newNode

    def Deque(self):
        if self.isEmpty():
            return
        if self.front is None:
            self.rear = None
            return
        temp = self.front.next
        self.front = temp

def dispalyNode(q):
    if q.front is None:
        print("Queue is empty")
    temp = q.front
    while temp is not None:
        print(temp.data , end=" ")
        temp = temp.next



if __name__ == '__main__':
    q = Queue()
    q.Enque(10)
    q.Enque(20)
    q.Enque(30)
    q.Enque(40)
    dispalyNode(q)

    q.Deque()
    print("\nAfter deque")
    dispalyNode(q)
