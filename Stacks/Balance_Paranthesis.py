class StackNode:
    def __init__(self, data=None):
        self.data = data
        self.next = None


class Stack:
    def __init__(self):
        self.root = None

    def isEmpty(self):
        return True if self.root is None else False

    def peek(self):
        if self.isEmpty():
            return float('-inf')
        else:
            return self.root.data

    def push(self, item):
        newNode = StackNode(item)
        newNode.next = self.root
        self.root = newNode
        print(item, " pushed to stack")

    def pop(self):
        if self.isEmpty():
            print("Stack is empty")
            return float('-inf')
        else:
            temp = self.root
            self.root = self.root.next
            print(temp.data, " is popped from stack")
            return temp.data

    def checkMatch(self, openBr, closeBr):
        if openBr == '[':
            return True if closeBr == ']' else False
        if openBr == '{':
            return True if closeBr == '}' else False
        if openBr == '(':
            return True if closeBr == ')' else False
        else:
            return False

    def checkBalanced(self, input):
        openBr = ['[', '{', '(']
        closeBr = [']', '}', ')']

        for symbol in input:
            if symbol in openBr:
                self.push(symbol)
            elif symbol in closeBr:
                poppedSymbol = self.pop()
                if self.checkMatch(poppedSymbol, symbol):
                    continue
                else:
                    return False
            else:
                continue
        return True if self.root is None else False


s = Stack()

print(s.checkBalanced("[(a+b)+(c)]"))