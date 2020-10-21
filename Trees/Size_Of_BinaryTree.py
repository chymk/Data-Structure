def SizeOfBinaryTree(root):
    if root is None:
        return 0
    return SizeOfBinaryTree(root.left)+SizeOfBinaryTree(root.right)+1

def findSizeUSingLevelOrder(root):
    if root is None:
        return 0
    size = 0
    q = Queue()
    q.enque(root)
    node = root
    while not q.isEmpty():
        node =q.deque()
        size += 1
        if node.left is not None:
            q.enque(node.left)
        if node.right is not None:
            q.enque(node.right)
    return size