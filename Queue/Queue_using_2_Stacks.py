class Queue:
    def __init__(self):
        self.s1 = []
        self.s2 = []
    def enqueue(self,item):
        if self.s1:
            while self.s1 :
                self.s2.append(self.s1.pop())
            self.s1.append(item)
            while self.s2:
                self.s1.append(self.s2.pop())
        else:
            self.s1.append(item)
    def dequeue(self):
        return self.s1.pop()

def displayQueue(q):
    print(q.s1)


q= Queue()
q.enqueue(1)
q.enqueue(2)
q.enqueue(3)
q.enqueue(4)
displayQueue(q)
q.dequeue()
displayQueue(q)