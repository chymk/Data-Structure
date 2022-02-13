''''How to implement a stack which will support following operations in O(1) time complexity?
1) push() which adds an element to the top of stack.
2) pop() which removes an element from top of stack.
3) findMiddle() which will return middle element of the stack.
4) deleteMiddle() which will delete the middle element. '''

class DLLNode:
    def __init__(self, data):
        self.prev = None
        self.next = None
        self.data = data

class myStack:
    def __init__(self):
        self.head = None
        self.mid = None
        self.count = 0

def createMyStack():
    ms = myStack()
    ms.count = 0
    return ms

def push(ms, new_data):
    newDLL = DLLNode(new_data)
    newDLL.prev = None
    newDLL.next = ms.head
    ms.count+=1
    if ms.count == 1:
        ms.mid = newDLL
    else:
        ms.head.prev = newDLL
        if ms.count%2 != 0:
            ms.mid = ms.mid.prev
    ms.head = newDLL

def pop(ms):
    if ms.count == 0:
        print("stack is empty")
        return -1
    head = ms.head
    item = head.data
    ms.head = head.next

    if ms.head != None
        ms.head.prev = None
    ms.count-=1
    if ms.count % 2 == 0:
        ms.mid = ms.mid.next
    return item

def findMiddle(ms):
    if ms.count == 0:
        print("Stack is empty now")
        return -1
    return ms.mid.data





