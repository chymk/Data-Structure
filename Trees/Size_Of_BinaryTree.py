class Node:
    def __init__(self,data=None):
        self.data = data
        self.left = None
        self.right =None

def SizeOfBinaryTree(root):
    if root is None:
        return 0
    return SizeOfBinaryTree(root.left)+SizeOfBinaryTree(root.right)+1

def findSizeUSingLevelOrder(root):
    if root is None:
        return 0
    size = 0
    q = []
    q.append(root)
    node = root
    while q!=[]:
        node =q.pop(0)
        size += 1
        if node.left is not None:
            q.append(node.left)
        if node.right is not None:
            q.append(node.right)
    return size

if __name__== '__main__':
    root = Node(2)
    root.left = Node(7)
    root.right = Node(5)
    root.left.right = Node(6)
    root.left.right.left = Node(1)
    root.left.right.right = Node(11)
    root.right.right = Node(9)
    root.right.right.left = Node(4)

    print(SizeOfBinaryTree(root))
    print(findSizeUSingLevelOrder(root))
