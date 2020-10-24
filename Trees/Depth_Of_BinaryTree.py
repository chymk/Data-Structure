class Node:
    def __init__(self,data=None):
        self.data = data
        self.left = None
        self.right =None

def DepthOfBinaryTree(root):
    if root is None:
        return 0
    return max(DepthOfBinaryTree(root.left),DepthOfBinaryTree(root.right))+1

def Depth(root):
    if root is None:
        return 0
    q = []
    node = root
    q.append([root,1])
    temp = 0
    while len(q)!=0:
        node,depth = q.pop(0)
        temp = max(temp,depth)
        if node.left is not None:
            q.append([node.left,depth])
        if node.right is not None:
            q.append([node.right,depth])
    return temp


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
    print("Depth",Depth(root))