from sys import maxsize

def createStack():
    stack = []
    return stack

def isEmpty(stack):
    return len(stack) == 0

def push(stack,item):
    stack.append(item)
    print(item ," pushed to stack")

def pop(stack):
    if isEmpty(stack):
        return str(-maxsize-1)
    return stack.pop()

def peek(stack):
    if isEmpty(stack):
        return str(-maxsize-1)
    return stack[len(stack)-1]

stack = createStack()
push(stack,1)
push(stack,2)
push(stack,3)
push(stack,4)
push(stack,5)
push(stack,6)

print(stack)

print(pop(stack))

print(stack)
print(peek(stack))
