class Node:
    def __init__(self,data=None):
        self.data = data
        self.left = self.right = None
max = float('-infinity')
def findMaxNode(root):
    global max
    if root is None:
        return max
    if root.data > max:
        max= root.data
    findMaxNode(root.left)
    findMaxNode(root.right)
    return max

def MaximumNode(root):
    maximum = -99
    stack = []
    node = root
    while stack or node:

        if node:
            stack.append(node)
            node = node.left

        else:
            node = stack.pop()
            if node.data > maximum:
                maximum = node.data
            node = node.right
    return maximum

if __name__== '__main__':
    root = Node(2)
    root.left = Node(7)
    root.right = Node(5)
    root.left.right = Node(6)
    root.left.right.left = Node(1)
    root.left.right.right = Node(11)
    root.right.right = Node(9)
    root.right.right.left = Node(4)

    print(MaximumNode(root))