class Queue:
    def __init__(self):
        self.s1 = []
        self.s2 = []

    def enQueue(self,x):
        while len(self.s1)!=0:
            self.s2.append(self.s1[-1])
            self.s1.pop()
        self.s1.append(x)
        while len(self.s2)!=0:
            self.s1.append(self.s2[-1])
            self.s2.pop()

    def deQueue(self):
        if len(self.s1)==0:
            print("Stack is empty")
            return None
        return self.s1.pop()

Q=Queue()
print("Enque operation")
arr = [4,5,7,6]
for x in arr:
    Q.enQueue(x)
print("Deque operation")
for x in arr:
    print(Q.deQueue())
print(Q.deQueue())
