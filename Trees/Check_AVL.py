class Node:
    def __init__(self,data=None):
        self.data = data
        self.left = None
        self.right = None

def insert(root,key):
    temp = root
    if temp is None:
        return Node(key)
    else:
        if temp.data == key:
            return temp
        elif key < temp.data:
            root.left=insert(temp.left,key)
        else:
            root.right=insert(temp.right,key)
    return root

def height(root):
    if root:
        return max(height(root.left),height(root.right))+1
    return 0

def checkAVL(root):
    q = []
    q.append(root)
    temp = None
    balance = leftH = rightH = 0
    while q!=[]:
        temp = q.pop(0)
        if temp.left:
            leftH = height(root.left)
        if temp.right:
            rightH  = height(root.right)
        balance = leftH - rightH
        if balance >= -1 and balance <= 1:
            continue
        else:
            return False
    return True




def inorder(root):
    if root:
        inorder(root.left)
        print(root.data)
        inorder(root.right)


r = Node(50)
r = insert(r, 30)
r = insert(r, 20)
r = insert(r, 40)
r = insert(r, 70)
r = insert(r, 60)
r = insert(r, 80)

inorder(r)
print("is BST an AVL : ",checkAVL(r))