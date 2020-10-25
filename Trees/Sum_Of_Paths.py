class Node:
    def __init__(self,data=None):
        self.data = data
        self.left = None
        self.right =None
Sum = 0
def printPath(root):
    path = []
    printPathRec(root,path,0)

def printPathRec(root,path,pathLen):

    if root is None:
        return

    if len(path)>pathLen:
        path[pathLen] = root.data
    else:
        path.append(root.data)
    pathLen = pathLen+1
    global Sum
    if root.left is None and root.right is None:
        a = map(str, path[0:pathLen])
        a=int(''.join(a))
        Sum = Sum +a
        print(Sum)
    else:
        printPathRec(root.left,path,pathLen)
        printPathRec(root.right,path,pathLen)

if __name__== '__main__':
    root = Node(2)
    root.left = Node(7)
    root.right = Node(5)
    root.left.right = Node(6)
    root.left.right.left = Node(1)
    root.left.right.right = Node(3)
    root.right.right = Node(9)
    root.right.right.left = Node(4)


    printPath(root)