class TwoStacks:
    def __init__(self, n):
        self.size = n
        self.arr = [None] * n
        self.top1 = -1
        self.top2 = self.size

    def push1(self,item):
        if self.top1 < self.top2 -1:
            self.top1 += 1
            self.arr[self.top1] = item
            print("%d pushed into stack1"%item)
        else:
            print(" Stack Overflow")

    def push2(self,item):
        if self.top1 < self.top2 -1:
            self.top2 -= 1
            self.arr[self.top2] = item
            print("%d pushed into stack2"%item)
        else:
            print(" Stack Overflow")
            exit(1)

    def pop1(self):
        if self.top1 >= 0:
            x = self.arr[self.top1]
            self.top1 -= 1
            return x
        else:
            print("Stack Underflow")
            exit(1)

    def pop2(self):
        if self.top2 < self.size:
            x = self.arr[self.top2]
            self.top2 += 1
            return x
        else:
            print("Stack Underflow")
            exit(1)


s = TwoStacks(5)
s.push1(3)
s.push1(2)
s.push2(0)
s.push2(7)
s.push1(1)

s.push2(0)

print(s.pop1())
print(s.pop2())
