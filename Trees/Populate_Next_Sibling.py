'''Visit the root
While traversing L, keep all the elements l+1 in queue
Go the next level and visit all the nodes
Repeat until all the levels are completed'''

class Node:
    def __init__(self,data=None):
        self.data = data
        self.left = None
        self.right = None
        self.nextSibling = None


def populateNextSibling(root):
    if root is None:
        return None
    q = []
    q.append(root)
    node = None
    count = 0
    while q !=[]:
        node = q.pop(0)

        if node.left is not None:
            q.append(node.left)
        if node.right is not None:
            q.append(node.right)
        if node.left is not None or node.right is not None:
            node.nextSibling = q[-1]
    return node



def printLevel(root):
    while root:
        print(" ",root.data)
        root = root.nextSibling

if __name__== '__main__':
    root = Node(2)
    root.left = Node(7)
    root.right = Node(5)
    root.left.right = Node(6)
    root.left.right.left = Node(1)
    root.left.right.right = Node(3)
    root.right.right = Node(9)
    root.right.right.left = Node(4)



    root=populateNextSibling(root)
    printLevel(root)
