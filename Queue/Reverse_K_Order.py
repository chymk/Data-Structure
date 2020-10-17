class Node:
    def __init__(self,data=None):
        self.data = data
        self.next = None

class Stack:
    def __init__(self):
        self.root = None

    def isEmpty(self):
        return True if self.root is None else False

    def push(self,data):
        newNode = Node()
        newNode.data = data
        newNode.next = self.root

        self.root = newNode



    def peek(self):
        if self.isEmpty():
            return float('-inf')
        return self.root.data

    def pop(self):
        if self.isEmpty():
            return float('-inf')
        temp = self.root
        self.root = temp.next
        return temp.data

class Queue:
    def __init__(self):
        self.front = self.rear = None

    def isempty(self):
        return True if self.front is None else False

    def enque(self,item):
        newNode = Node(item)
        if self.rear is None:
            self.rear = self.front = newNode
            return
        self.rear.next = newNode
        self.rear = newNode

    def Deque(self):
        if self.isempty():
            return
        if self.front is None:
            self.rear = None
            return
        temp = self.front
        self.front = temp.next
        return temp.data

def dispalyQueue(q):
    if q.front is None:
        print("Q is empty")
        return
    temp = q.front
    while temp is not None:
        print(temp.data , end=" ")
        temp = temp.next
    print("")

def reverseKelements(Q,k):
    if Q.isempty():
        print("Q is empty")
        return
    stack = Stack()
    for i in range(k):
        if Q.isempty():
            print("K is greater than Queue Length")
            return
        stack.push(Q.Deque())

    q1 = Queue()
    while not stack.isEmpty():
        q1.enque(stack.pop())
    while not Q.isempty():
        q1.enque(Q.Deque())
    return q1



Q = Queue()
Q.enque(1)
Q.enque(2)
Q.enque(3)
Q.enque(4)
Q.enque(5)
Q.enque(6)

dispalyQueue(Q)
K=reverseKelements(Q,7)
if K is not None:
    dispalyQueue(K)