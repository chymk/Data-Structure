class newNode:
    def __init__(self,data=None):
        self.data = data
        self.left = None
        self.right = None

def Reverse_Morris_Traversal(root):
    if not root:
        return
    current = root
    successor = 0
    while current:
        if current.right is None:
            print(current.data,end=" ")
        else:
            successor = current.right

            while successor.left != None and successor.left!=current:
                successor = successor.left
            if successor.left == None:
                successor.left = current
                current = current.right
            else:
                successor.left = None
                print(current.data,end=" ")
                current=current.left


if __name__ == "__main__":
    """ Constructed binary tree is  
        1  
        / \  
    2     3  
    / \ / \  
    4 5 6 7  
"""

    root = newNode(1)
    root.left = newNode(2)
    root.right = newNode(3)
    root.left.left = newNode(4)
    root.left.right = newNode(5)
    root.right.left = newNode(6)
    root.right.right = newNode(7)

    # reverse inorder traversal.
    Reverse_Morris_Traversal(root)