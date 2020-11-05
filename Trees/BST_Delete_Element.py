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

def minValue(root):
    current = root
    while current.left:
        current = current.left
    return current


def delete(root,key):
    if root is None:
        return root

    if key < root.data:
        root.left = delete(root.left,key)

    elif key > root.data:
        root.right = delete(root.right,key)

    else:
        # Node with only one child or no child
        if root.left is None:
            temp = root.right
            root = None
            return temp
        if root.right is None:
            temp = root.left
            root = None
            return temp

        # Node with only Two child
        temp = minValue(root.right)
        root.data = temp.data
        root.right = delete(root.right,temp.data)
    return root


r = Node(50)
r = insert(r, 30)
r = insert(r, 20)
r = insert(r, 40)
r = insert(r, 70)
r = insert(r, 60)
r = insert(r, 80)

printInorder(r)
delete(r,30)
print("")
printInorder(r)

