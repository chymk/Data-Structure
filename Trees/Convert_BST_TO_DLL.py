class Node:
    def __init__(self,data=None):
        self.data = data
        self.left = None
        self.right = None

def insert(root,key):
    temp = root
    if temp is None:
        return Node(key)
    else:
        if temp.data == key:
            return temp
        elif key < temp.data:
            root.left=insert(temp.left,key)
        else:
            root.right=insert(temp.right,key)
    return root

prev = None
head = None

def convert(root):
    global prev
    global head
    if root is None:
        return
    convert(root.left)

    if prev is None:
        head = root
        print(head.data,"root")
    else:
        root.left = prev
        prev.right = root

    prev = root
    convert(root.right)
    return head

def inorder(root):
    if root:
        inorder(root.left)
        print(root.data)
        inorder(root.right)

def printDLL(root):
    current = root
    while current:
        print(current.data,end=" ")
        current = current.right

r = Node(50)
r = insert(r, 30)
r = insert(r, 20)
r = insert(r, 40)
r = insert(r, 70)
r = insert(r, 60)
r = insert(r, 80)


head= convert(r)
printDLL(head)

