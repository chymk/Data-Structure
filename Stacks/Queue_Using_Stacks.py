def enqueue(x, stack1, stack2):
    '''
    x: value to push
    stack1: list
    stack2: list
    '''
    while len(stack1) != 0:
        p = stack1.pop()
        stack2.append(p)
    stack1.append(x)
    while len(stack2) != 0:
        q = stack2.pop()
        stack1.append(q)



def dequeue(stack1, stack2):
    '''
    stack1: list
    stack2: list
    '''
    if len(stack1) == 0:
        return -1
    s = stack1[-1]
    stack1.pop()
    return s

    # code here