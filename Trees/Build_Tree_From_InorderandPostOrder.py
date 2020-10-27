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

def buildtree(inOrder,postOrder):
    if len(inOrder)<1:
        return None
    root = Node(postOrder[-1])
    rootPos = inOrder.index(postOrder[-1])
    root.left = buildtree(postOrder[:rootPos],inOrder[:rootPos])
    root.right = buildtree(postOrder[rootPos:-1],inOrder[rootPos+1:])
    return root

def printInorder(root):
    if root is None:
        return
    printInorder(root.left)
    print(root.data, end=" ")
    printInorder(root.right)

root = buildtree([4, 8, 2, 5, 1, 6, 3, 7],[8, 4, 5, 2, 6, 7, 3, 1])
printInorder(root)