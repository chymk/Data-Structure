'''Visit the root
While traversing L, keep all the elements l+1 in queue
Go the next level and visit all the nodes
Repeat until all the levels are completed'''

class Node:
    def __init__(self,data=None):
        self.data = data
        self.left = None
        self.right = None

def ZigZagTraversal(root):
    if root is None:
        return
    # create current and next Level
    currentLevel = []
    nextLevel = []

    #if ltr is true push nodes from left to right else right to left
    ltr = True

    currentLevel.append(root)

    #Check if stack is empty
    while len(currentLevel)>0:

        temp = currentLevel.pop()
        print(temp.data,end=" ")

        if ltr:
            if temp.left:
                nextLevel.append(temp.left)
            if temp.right:
                nextLevel.append(temp.right)
        else:
            if temp.right:
                nextLevel.append(temp.right)
            if temp.left:
                nextLevel.append(temp.left)

        if len(currentLevel)==0:
            #reverse ltr to push in opposite direction
            ltr = not ltr
            #swap stacks
            currentLevel,nextLevel = nextLevel,currentLevel



if __name__== '__main__':
    root = Node(2)
    root.left = Node(7)
    root.right = Node(5)
    root.left.right = Node(6)
    root.left.right.left = Node(1)
    root.left.right.right = Node(3)
    root.right.right = Node(9)
    root.right.right.left = Node(4)

    ZigZagTraversal(root)
