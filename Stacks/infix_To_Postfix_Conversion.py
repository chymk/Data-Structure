class Conversion:
    def __init__(self,capacity):
        self.capacity = capacity
        self.top = -1
        self.output = []
        self.array = []
        self.precedence = {'+':1,'-':1,'*':2,'/':2,'^':3}

    def isEmpty(self):
        return True if self.top ==-1 else False

    def peek(self):
        return self.array[-1]

    def pop(self):
        if not self.isEmpty():
            self.top -= 1
            return self.array.pop()
        else:
            return -1

    def push(self,op):
        self.top += 1
        self.array.append(op)

    def isOperand(self,ch):
        return ch.isalpha()

    def notGreater(self, i):
        try:
            a = self.precedence[i]
            b = self.precedence[self.peek()]
            return True if a <= b else False
        except KeyError:
            return False

    def infixToPostfix(self,exp):
        for i in exp:
            print("Char to Convert ",i)
            if self.isOperand(i):
                self.output.append(i)

            elif i == '(':
                self.push(i)
            # If the scanned character is an ')', pop and
            # output from the stack until and '(' is found
            elif i == ')':
                while (not self.isEmpty()) and self.peek()!='(':
                    a = self.pop()
                    self.output.append(a)
                if (not self.isEmpty()) and self.peek() != '(':
                    print("Return")
                    return -1
                else:
                    self.pop()

            else:
                while (not self.isEmpty()) and self.notGreater(i):
                    self.output.append(self.pop())
                self.push(i)
            print("Stack ",self.array)
            print("Output ",self.output)
        while not self.isEmpty():
            self.output.append(self.pop())
        print("".join(self.output))

exp = "A*(B+C)/D"
obj = Conversion(len(exp))
obj.infixToPostfix(exp)









