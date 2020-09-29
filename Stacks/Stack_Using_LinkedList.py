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

stack = Stack()
stack.push(10)
stack.push(20)
stack.push(30)
print("Top element is % d " % (stack.peek()))
print("% d popped from stack" % (stack.pop()))
