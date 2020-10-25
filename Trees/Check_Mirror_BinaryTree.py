class Node:
    def __init__(self,data=None):
        self.data = data
        self.left = None
        self.right =None

def CheckMirror(root1,root2):
    if root1 is None and root2 is None:
        return 1
    if root1 is None or root2 is None:
        return 0
    if root1.data != root2.data:
        return 0
    return CheckMirror(root1.left,root2.right) and CheckMirror(root1.right,root2.left)




if __name__== '__main__':
    root = Node(2)
    root.left = Node(7)
    root.right = Node(5)
    root.left.right = Node(6)
    root.left.right.left = Node(1)
    root.left.right.right = Node(3)
    root.right.right = Node(9)
    root.right.right.left = Node(4)

    root1 = Node(2)
    root1.right = Node(7)
    root1.left = Node(5)
    root1.right.left = Node(6)
    root1.right.left.right = Node(1)
    root1.right.left.left = Node(3)
    root1.left.left = Node(9)
    root1.left.left.right = Node(4)
    print(CheckMirror(root,root1))
