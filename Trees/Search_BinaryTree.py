from collections import deque

class Node:
    def __init__(self,data=None):
        self.data = data
        self.left = self.right = None


def recursiveSearch(root,data):
    if not root:
        return 0
    if root.data == data:
        return 1
    else:
        temp = recursiveSearch(root.left,data)
        if temp == 1:
            return 1
        else:
            return recursiveSearch(root.right,data)

def searchData(root,data):
    if not root:
        return 1
    q = deque()
    q.enque(root)
    node = root
    while not q.isempty()
        node = q.dequeue()
        if node.data == data:
            return 1
        else:
            if node.left:
                q.enque(node.left)
            if node.right:
                q.enque(node.right)
    return 0

if __name__== '__main__':
    root = Node(2)
    root.left = Node(7)
    root.right = Node(5)
    root.left.right = Node(6)
    root.left.right.left = Node(1)
    root.left.right.right = Node(11)
    root.right.right = Node(9)
    root.right.right.left = Node(4)

    print(recursiveSearch(root,9))