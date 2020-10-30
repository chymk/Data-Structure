class Node:
    def __init__(self,key):
        self.key = key
        self.left = None
        self.right = None
        self.isThreaded = False

def populateQueue(root,q):
    if root == None: return
    if root.left:
        populateQueue(root.left,q)
    q.append(root)
    if root.right:
        populateQueue(root.right,q)

def createThreadedUtill(root,q):
    if root == None: return
    if root.left:
        createThreadedUtill(root.left,q)
    q.pop(0)
    if root.right:
        createThreadedUtill(root.right,q)
    #If right pointer is None, link it to the inorder successor and set isThreaded
    else:
        if len(q)==0:
            root.right=None
        else:
            root.right = q[0]
            root.isThreaded = True

def createThreaded(root):
    q=[]
    populateQueue(root,q)
    createThreadedUtill(root,q)

def leftMost(root):
    while root!=None and root.left != None:
        root= root.left
    return root

def inorder(root):
    if root == None:
        return
    cur = leftMost(root)
    while cur!=None:
        print(cur.key,end=" ")
        if cur.isThreaded:
            cur = cur.right
        else:
            cur = leftMost(cur.right)


if __name__ == "__main__":
    root = Node(1)
    root.left = Node(2)
    root.right = Node(3)
    root.left.right = Node(5)
    root.left.left = Node(4)
    root.right.left = Node(6)
    root.right.right = Node(7)

    createThreaded(root)

    print("Inorder traversal of created threaded tree is")
    inorder(root)

