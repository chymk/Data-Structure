class Node:
    def __init__(self,data=None):
        self.data = data
        self.left = None
        self.right = None

def insert(root,key):
    if root is None:
        return Node(key)
    if key == root.data:
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

def findMin(root):
    current = root
    if current.left is None:
        return current.data
    else:
        return findMin(current.left)

def findMinIterate(root):
    current = root
    if current is None:
        return current
    while current.left:
        current = current.left
    return current.data

r = Node(50)
r = insert(r, 30)
r = insert(r, 20)
r = insert(r, 40)
r = insert(r, 70)
r = insert(r, 60)
r = insert(r, 80)

print(findMin(r))
print(findMinIterate(r))
