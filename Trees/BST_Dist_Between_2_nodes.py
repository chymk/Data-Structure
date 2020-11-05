class Node:
    def __init__(self,data=None):
        self.data = data
        self.left = None
        self.right = None

def insert(root,key):
    if root is None:
        return Node(key)
    if root.data == key:
        return root
    if key < root.data:
        root.left = insert(root.left,key)
    else:
        root.right = insert(root.right,key)
    return root

def printInorder(root):
    if root:
        printInorder(root.left)
        print(root.data,end=" ")
        printInorder(root.right)


def findLCA(root,a,b):
    while root:
        if (a<=root.data and b>root.data) or (a>root.data and b<=root.data):
            return root
        if a < root.data:
            root = root.left
        else:
            root = root.right

def distFromRoot(root,x):
    dist = 0
    if root is None:
        return 0
    current = root
    while current:
        dist += 1
        if current.data == x:
            return dist -1
        elif x < current.data:
            current = current.left
        else:
            current = current.right

def distBetweenNodes(root,a,b):
    LCA = findLCA(root,a,b)
    return distFromRoot(LCA,a)+distFromRoot(LCA,b)






r = Node(50)
r = insert(r, 30)
r = insert(r, 20)
r = insert(r, 40)
r = insert(r, 70)
r = insert(r, 60)
r = insert(r, 80)

printInorder(r)

print("")
print(distBetweenNodes(r,20,70))

