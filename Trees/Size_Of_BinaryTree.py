def SizeOfBinaryTree(root):
    if root is None:
        return 0
    return SizeOfBinaryTree(root.left)+SizeOfBinaryTree(root.right)+1