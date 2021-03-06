class Node:
    def __init__(self,data=None):
        self.data = data
        self.left = self.right = None

def levelOrderTraversalReverse(root):
    if root is None:
        print("Stack is empty")
        return
    queue = []
    stack = []
    queue.append(root)
    node = None
    while queue != []:
        node = queue.pop(0)
        if node.left is not None:
            queue.append(node.left)
        if node.right is not None:
            queue.append(node.right)
        stack.append(node)
    while stack !=[]:
        node = stack.pop()
        print(node.data,end=" ")


if __name__== '__main__':
    root = Node(2)
    root.left = Node(7)
    root.right = Node(5)
    root.left.right = Node(6)
    root.left.right.left = Node(1)
    root.left.right.right = Node(11)
    root.right.right = Node(9)
    root.right.right.left = Node(4)

    levelOrderTraversalReverse(root)
