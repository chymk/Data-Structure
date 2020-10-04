class StackNode:
    def __init__(self):
        self.data = None
        self.next = None

class Stack:
    def __init__(self):
        self.root = None

    def isEmpty(self):
        return True if self.root is None else False

    def push(self,data):
        newNode = StackNode()
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

class SpecialStack(Stack):
    def __init__(self):
        self.min = Stack()

    def push(self,x):
        if Stack.isEmpty():
            self.push(x)
            self.min.push(x)
        else:
            Stack.push(x)
            y = self.min.pop()
            self.min.push(y)
            if(x<y):
                self.min.push(x)
            else:
                self.min.push(y)

    def pop(self):
        self.min.pop()
        Stack.pop()

    def getMin(self):
        return self.min.peek()

s  = SpecialStack()
s.push(21)
s.push(14)
s.push(17)
s.push(2)
s.push(7)
s.push(19)

s.getMin()






