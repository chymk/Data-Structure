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

def printRange(root,K1,K2):
    if root:
        printRange(root.left,K1,K2)
        if root.data >= K1 and root.data <= K2:
            print(root.data)
        printRange(root.right,K1,K2)


r = Node(50)
r = insert(r, 30)
r = insert(r, 20)
r = insert(r, 40)
r = insert(r, 70)
r = insert(r, 60)
r = insert(r, 80)

printRange(r,40,70)