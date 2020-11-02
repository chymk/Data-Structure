class Node:
    def __init__(self,data=None):
        self.data = data
        self.left = self.right = None

def findLCA(root,n1,n2):
    if root is None:
        return None
    '''IF either of n1 and n2 found report the presence by returning node'''
    if root.data == n1 or root.data == n2:
        return root

    leftLCA = findLCA(root.left,n1,n2)
    rightLCA = findLCA(root.right,n1,n2)

    if leftLCA and rightLCA:
        return root

    return leftLCA if leftLCA is not None else rightLCA



if __name__== '__main__':
    root = Node(2)
    root.left = Node(7)
    root.right = Node(5)

    root.left.right = Node(6)
    root.left.right.left = Node(1)
    root.left.right.right = Node(11)
    root.right.right = Node(9)
    root.right.right.left = Node(4)

    print(findLCA(root,11,5).data)