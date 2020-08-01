'''
You are given a BST data structure consisting of BST nodes. Each BST node has an integer value stored in a property called "value" and two children nodes stored
in properties called "left" and "right," respectively. A node is said to be a BST node if and only if it satises the BST property: its value is strictly greater than the
values of every node to its left; its value is less than or equal to the values of every node to its right; and both of its children nodes are either BST nodes
themselves or None (null) values. You are also given a target integer value; write a function that nds the closest value to that target value contained in the BST.
Assume that there will only be one closest value.
Sample input:
        10 , 12
       /  \
      5   15
     / \   / \
    2   5 13 22
   /        \
  1         14
Sample output: 13
'''

class node:
    def __init__(self, data):
        self.left = None
        self.right = None
        self.data = data

    def insert(self, newVal):
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
            self = node(newVal)

    def printTree(self):
        if self.left is not None:
            self.left.printTree()
        print(self.data)
        if self.right is not None:
            self.right.printTree()

    def closestValuess(self, root, target):
        return self.closestValue(self, target, float("inf"))

    def closestValue(self,root,target,closest):
        currentNode = root
        while currentNode is not None:
            t1 = abs(closest - target)
            t2 = abs(currentNode.data - target)
            if t2 < t1:
                closest = currentNode.data
            if currentNode.data > target:
                currentNode = currentNode.left
            elif currentNode.data < target:
                currentNode = currentNode.right
            else:
                break
        return closest

root = node(10)
root.insert(5)
root.insert(2)
root.insert(1)
root.insert(5)
root.insert(15)
root.insert(13)
root.insert(22)
root.insert(14)

print(root.closestValuess(root, 19))
