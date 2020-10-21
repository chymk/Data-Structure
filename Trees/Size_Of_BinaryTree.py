def SizeOfBinaryTree(root):
    if root is None:
        return 0
    return SizeOfBinaryTree(root.left)+SizeOfBinaryTree(root.right)+1

def findSizeUSingLevelOrder(root):
    if root is None:
        return 0
    q = Queue()
    q.enque(root)
    node = root
    while not q.isEmpty():
