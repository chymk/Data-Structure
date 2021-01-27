class TreeNode:
    def __init__(self, data=None):
        self.data = data
        self.left = None
        self.right = None


def findPathSum(root):
    return pathSum(root, 0)


def pathSum(root, path):
    if root is None:
        return 0
    path = 10 * path + root.data
    if root.left is None and root.right is None:
        return path
    return (pathSum(root.left, path) + pathSum(root.right, path))

root = TreeNode(1)
root.left = TreeNode(0)
root.right = TreeNode(1)
root.left.left = TreeNode(1)
root.right.left  = TreeNode(6)
root.right.right = TreeNode(5)
print(findPathSum(root))