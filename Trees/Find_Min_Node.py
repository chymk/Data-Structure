class Node:
    def __init__(self,data=None):
        self.data = data
        self.left = self.right = None
min = float('infinity')
def findMinimum(root):
    global min
    if root is None:
        return min
    if root.data < min:
        min = root.data
    findMinimum(root.left)
    findMinimum(root.right)
    return min

if __name__== '__main__':
    root = Node(2)
    root.left = Node(7)
    root.right = Node(5)
    root.left.right = Node(6)
    root.left.right.left = Node(1)
    root.left.right.right = Node(11)
    root.right.right = Node(9)
    root.right.right.left = Node(4)

    print(findMinimum(root))