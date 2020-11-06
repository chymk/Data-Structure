class Node:
    def __init__(self,data = None):
        self.data = data
        self.left = self.right = None

def concaltenate(leftList,rightList):
    if leftList is None:
        return rightList
    if rightList is None:
        return leftList

    leftLast = leftList.left
    rightLast = rightList.left

    leftLast.right = rightList
    rightLast.left = leftLast

    leftList.left = rightLast
    rightLast.right = leftList
    return leftList

def bTreeToCLL(root):
    if root is None:
        return None

    left = bTreeToCLL(root.left)
    right = bTreeToCLL(root.right)


    # Make a circular linked list of single node (or root). To do so, make the
    # right and left pointers of this node
    # point to itself
    root.left = root.right = root

    return concaltenate(concaltenate(left,root),right)