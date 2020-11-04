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

def predecessor(root):
    current = root
    if current is None:
        return None
    if current.left:
        current = current.left
        while current.right:
            current = current.right
        return current.data

def successor(root):
    current = root
    if current is None:
        return None
    if current.right:
        current = current.right
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

print("Predecessor : ",predecessor(r))
print("Successor : ",successor(r))
