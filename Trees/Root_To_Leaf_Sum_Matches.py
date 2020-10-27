class Node:
    def __init__(self,data=None):
        self.data = data
        self.left = None
        self.right = None


def rootToLeafSumMatch(root,Sum):
    if root is None:
        return False
    if root.left is None and root.right is None and Sum == root.data:
        return True

    if rootToLeafSumMatch(root.left,Sum-root.data):
        return True
    if rootToLeafSumMatch(root.right,Sum-root.data):
        return True
    return False


if __name__== '__main__':
    root = Node(2)
    root.left = Node(7)
    root.right = Node(5)
    root.left.right = Node(6)
    root.left.right.left = Node(1)
    root.left.right.right = Node(11)
    root.right.right = Node(9)
    root.right.right.left = Node(4)


    print(rootToLeafSumMatch(root,20))




