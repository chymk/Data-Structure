'''
Write an algorithm to calculate all branch sums left to right.

Sample input:
        10
       /  \
      5   15
     / \   / \
    2   5 13 22
   /        \
  1         14
  '''

class node:
    def __init__(self,data):
        self.left = None
        self.right = None
        self.data = data

    def insert(self,newVal):
        if self.data:
            if newVal < self.data:
                if self.left is None:
                    self.left = node(newVal)
                else:
                    self.left.insert(newVal)
            else:
                if self.right is None:
                    self.right = node(newVal)
                else:
                    self.right.insert(newVal)
        else:
            self.data =newVal

    def printTree(self):
        if self.left is not None:
            self.left.printTree()
        print(self.data)
        if self.right is not None:
            self.right.printTree()


def bSum(root, sums=[], branchSum=0):
    if root is None:
        return

    if sums is None:
        sums = []
    branchSum += root.data
    #print(root.data)
    if root.left is None and root.right is None:
        sums.append(branchSum)
        return
    bSum(root.left, sums, branchSum)
    bSum(root.right, sums, branchSum)
    return sums

root = node(10)
root.insert(5)
root.insert(2)
root.insert(1)
root.insert(5)
root.insert(15)
root.insert(13)
root.insert(22)
root.insert(14)

print(bSum(root))



