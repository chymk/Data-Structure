class Node:
    def __init__(self,data=None):
        self.data = data
        self.left = None
        self.right =None

def mirror(root):
    if root is None:
        return
    mirror(root.left)
    mirror(root.right)
    temp = root.left
    root.left = root.right
    root.right = temp
    return root

if __name__== '__main__':
    root = Node(2)
    root.left = Node(7)
    root.right = Node(5)
    root.left.right = Node(6)
    root.left.right.left = Node(1)
    root.left.right.right = Node(3)
    root.right.right = Node(9)
    root.right.right.left = Node(4)

    mirror(root)
    print(root.left.data)
    print(root.right.data)