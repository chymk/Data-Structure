class Stack:
    def __init__(self):
        self.items=[]

    def isEmpty(self):
        if self.items == []:
            return True
        else:
            return False

    def peek(self):
        return self.items[-1]

    def pop(self):
        return self.items.pop()

    def push(self,k):
        self.items.append(k)

def findingSpans(A):
    s = [None]*len(A)
    s[0]=1
    for i in range(1,len(A),1):
        j=i-1
        s[i]=1
        while j>=0 and A[i]>=A[j]:
            s[i]+=1
            j-=1
    return s

def findingSpans2(A):
    s = [None]*len(A)
    d =Stack()
    for i in range(0,len(A)):
        while not d.isEmpty() and A[i]>=A[d.peek()]:
            d.pop()
        if d.isEmpty():
            p = -1
        else:
            p = d.peek()
        s[i] = i-p
        d.push(i)
    return s

S = Stack()
S.push(6)
S.push(3)
S.push(4)
S.push(5)
S.push(2)


print(findingSpans(S.items))


