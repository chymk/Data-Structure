class Node:
    def __init__(self,data=None):
        self.data = data
        self.left = None
        self.right =None

def DepthOfBinaryTree(root):
    if root is None:
        return 0
    return max(DepthOfBinaryTree(root.left),DepthOfBinaryTree(root.right))+1

def findDepthUSingLevelOrder(root):
    if root is None:
        return 0
    depthLeft = 0
    depthRight = 0
    q = []
    q.append(root)
    node = root
    while q!=[]:
        node =q.pop(0)
        if node.left is not None:
            q.append(node.left)
            depthLeft += 1
        if node.right is not None:
            q.append(node.right)
            depthRight += 1
    return max(depthLeft,depthRight)+1

if __name__== '__main__':
    root = Node(2)
    root.left = Node(7)
    root.right = Node(5)
    root.left.right = Node(6)
    root.left.right.left = Node(1)
    root.left.right.right = Node(11)
    root.right.right = Node(9)
    root.right.right.left = Node(4)

    print(DepthOfBinaryTree(root))
    print(findDepthUSingLevelOrder(root))