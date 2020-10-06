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
            return False
        return self.root.data

    def pop(self):
        if self.isEmpty():
            return float('-inf')
        temp = self.root
        self.root = temp.next
        return temp.data

    def recursiveReverse(self, newStack):
        if not self.isEmpty():
            newStack.push(self.pop())
            self.recursiveReverse(newStack)
        return newStack

    def reverse(self):
        newStack =Stack()
        return self.recursiveReverse(newStack)

    def display(self):

        iternode = self.root
        if self.isEmpty():
            print("Stack Underflow")

        else:

            while (iternode != None):
                print(iternode.data, "->", end=" ")
                iternode = iternode.next
            return


stack = Stack()
stack.push(10)
stack.push(20)
stack.push(30)
stack.push(40)
stack.display()
newStack = Stack()
print("")
stack = stack.reverse()
stack.display()






