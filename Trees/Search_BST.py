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

def inorder(root):
    if root:
        inorder(root.left)
        print(root.data,end = " ")
        inorder(root.right)

def search(root,key):
    if root is None or root.data == key:
        return root
    if root.right and root.data < key:
        return search(root.right,key)
    elif root.left and root.data > key:
        return search(root.left,key)



r = Node(50)
r = insert(r, 30)
r = insert(r, 20)
r = insert(r, 40)
r = insert(r, 70)
r = insert(r, 60)
r = insert(r, 80)


print(search(r,10).data)