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

        if node.left:
            q.append(node.left)
        if node.right:
            q.append(node.right)
            #print([a.data for a in q])
        if q!=[]:
            node.nextSibling = q[0]

    return node




def printLevel(root):
    while root:
        print(root.data,end=" ")
        root = root.nextSibling

if __name__== '__main__':
    root = Node(1)
    root.left = Node(2)
    root.right = Node(3)
    root.left.right = Node(5)
    root.left.left = Node(4)
    root.right.right = Node(7)
    root.right.left = Node(6)



    populateNextSibling(root)
    printLevel(root)

