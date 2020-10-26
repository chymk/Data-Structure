class Node:
    def __init__(self,data=None):
        self.data = data
        self.left = None
        self.right = None

"""Recursive function to construct binary of size len from 
   Inorder traversal in[] and Preorder traversal pre[].  Initial values 
   of inStrt and inEnd should be 0 and len -1.  The function doesn't 
   do any error checking for cases where inorder and preorder 
   do not form a tree """

def buildtree(preOrder,inOrder):
    if len(inOrder)<1:
        return None
    root = Node(preOrder[0])
    rootPos = inOrder.index(preOrder[0])
    root.left = buildtree(preOrder[1:1+rootPos],inOrder[:rootPos])
    root.right = buildtree(preOrder[rootPos+1:],inOrder[rootPos+1:])
    return root

def printInorder(root):
    if root is None:
        return
    printInorder(root.left)
    print(root.data,end=" ")
    printInorder(root.right)

root = buildtree(['A','B','D','E','C','F'],['D','B','E','A','F','C'])
printInorder(root)