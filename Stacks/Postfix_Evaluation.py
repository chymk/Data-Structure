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

def postfixEvaluation(postExpr):
    stack = createStack()
    pstExpr = list(postExpr)
    print(postExpr)
    for i in postExpr:
        print(i)
        if i in ['1','2','3','4','5','6','7','8','9','0']:
            push(stack,int(i))
        else:
            op2 = pop(stack)
            op1 = pop(stack)
            x = doMath(i,op1,op2)
            push(stack,x)
    return pop(stack)

def doMath(op, op1, op2):
    if op == "*":
        return op1 * op2
    elif op == "/":
        return op1 / op2
    elif op == "+":
        return op1 + op2
    else:
        return op1 - op2




print(postfixEvaluation("173+*2/"))
