'''Visit the root
While traversing L, keep all the elements l+1 in queue
Go the next level and visit all the nodes
Repeat until all the levels are completed'''

class Node:
    def __init__(self,data=None):
        self.data = data
        self.left = None
        self.right = None


def


if __name__== '__main__':
    root = Node(2)
    root.left = Node(7)
    root.right = Node(5)
    root.left.right = Node(6)
    root.left.right.left = Node(1)
    root.left.right.right = Node(3)
    root.right.right = Node(9)
    root.right.right.left = Node(4)


    verticalSum(root,0)
    print(hashtable)
