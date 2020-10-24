class Node:
    def __init__(self,data=None):
        self.data = data
        self.left = None
        self.right =None

def countOfLeafNodes(root):
    if root is None:
        return 0
    q = []
    node = root
    q.append(root)
    count = 0
    while len(q)!=0:
        node = q.pop(0)
        if node.left is None and node.right is None:
            count += 1
        if node.left is not None:
            q.append(node.left)
        if node.right is not None:
            q.append(node.right)
    return count


if __name__== '__main__':
    root = Node(2)
    root.left = Node(7)
    root.right = Node(5)
    root.left.right = Node(6)
    root.left.right.left = Node(1)
    root.left.right.right = Node(11)
    root.right.right = Node(9)
    root.right.right.left = Node(4)

    #print(DepthOfBinaryTree(root))
    print("Leaves",countOfLeafNodes(root))