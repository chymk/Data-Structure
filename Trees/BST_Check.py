class Node:
    def __init__(self,data=None):
        self.data = data
        self.left = None
        self.right = None

def insert(root,key):
    if root is None:
        return Node(key)
    if root.data == key:
        return root
    if key < root.data:
        root.left = insert(root.left,key)
    else:
        root.right = insert(root.right,key)
    return root

def printInorder(root):
    if root:
        printInorder(root.left)
        print(root.data,end=" ")
        printInorder(root.right)


def checkBST(root):
    if root is None:
        return 1
    if root.left and root.left.data > root.data:
        return 0
    if root.right and root.right.data < root.data:
        return 0
    if not(checkBST(root.left) and checkBST(root.right)):
        return 0
    return 1





r = Node(50)
r = insert(r, 30)
r = insert(r, 20)
r = insert(r, 40)
r = insert(r, 70)
r = insert(r, 60)
r = insert(r, 80)

printInorder(r)
print("")
print(checkBST(r))


