class Node:
    def __init__(self,data=None):
        self.data = data
        self.left = None
        self.right =None

def height(root):
    if root is None:
         return 0
    return 1+max(height(root.left),height(root.right))

def diameter(root):
    if root is None:
        return 0
    #Get the height of left and right tree
    lheight = height(root.left)
    rheight = height(root.right)

    #Get the diameter of left and right diameter
    lDiameter = diameter(root.left)
    rDiameter = diameter(root.right)

    return max(lheight+rheight+1,max(lDiameter,rDiameter))

class Height:
    def __init__(self):
        self.h = 0

def opDiameter(root,height):
    lh = Height()
    rh = Height()
    if root is None:
        height.h = 0
        return 0
    ldiameter = opDiameter(root.left,lh)
    rDiameter = opDiameter(root.right,rh)

    height.h = max(lh.h,rh.h)+1

    return max(lh.h+rh.h+1,max(ldiameter,rDiameter))


def diameterr(root):
    h = Height()
    return opDiameter(root, h)



if __name__== '__main__':
    root = Node(2)
    root.left = Node(7)
    root.right = Node(5)
    root.left.right = Node(6)
    root.left.right.left = Node(1)
    root.left.right.right = Node(11)
    root.right.right = Node(9)
    root.right.right.left = Node(4)


    print("Diameter : ",diameterr(root))