
class Node:
    def __init__(self,data=None):
        self.data= data
        self.prev = None
        self.next = None

class DLL:
    def __init__(self):
        self.head = None
    def insert(self,data):
        newNode = Node(data)
        if self.head is None:
            return newNode
        current = self.head
        while current.next:
            current = current.next
        current.next = newNode
        newNode.prev = current


def findMiddle(head):
    return


def DLLToBST(head):
    if head is None or head.next is None:
        return head
    temp = findMiddle(head)
    current = head
    while current!=temp:
        current = current.next
    current.next = None
    q = temp.next
    temp.next is None
    temp.prev = DLLToBST(head)
    temp.next = DLLToBST(q)
    return temp

def inorder(root):
    inorder(root.prev)
    print(root.data)
    inorder(root.right)
