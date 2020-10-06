class Stack:
    def __init__(self):
        self.items=[]

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

S = Stack()
S.push(10)
S.push(4)
S.push(5)
S.push(90)
S.push(120)
S.push(80)

print(findingSpans(S.items))


