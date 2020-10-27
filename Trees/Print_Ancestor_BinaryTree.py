class Node:
    def __init__(self,data=None):
        self.data = data
        self.left = None
        self.right = None

def printAncestor(root,node):
    if root is None:
        return 0
    if root.left==node or root.right == node or printAncestor(root.left,node) or printAncestor(root.right,node):
        print(root.data)
        return 1
    return 0



if __name__== '__main__':
    root = Node(2)
    root.left = Node(7)
    root.right = Node(5)
    root.left.right = Node(6)
    root.left.right.left = Node(1)
    root.left.right.right = Node(11)
    root.right.right = Node(9)
    root.right.right.left = Node(4)

    printAncestor(root,root.right.right.left)


