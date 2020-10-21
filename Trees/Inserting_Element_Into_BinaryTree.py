class BinaryTree:
    def __init__(self,data=None):
        self.data = data
        self.left = None
        self.right = None

    def getData(self):
        return self.data

    def setData(self,data):
        self.data = data

    def getLeft(self):
        return self.left

    def getRight(self):
        return self.right

    def insertLeft(self,newNode):
        if self.left is None:
            self.left = BinaryTree(newNode)
        else:
            temp = BinaryTree(newNode)
            temp.left = self.left
            self.left = temp

    def insertRight(self,newNode):
        if self.right is None:
            self.right = BinaryTree(newNode)
        else:
            temp = BinaryTree(newNode)
            temp.right = self.right
            self.right = temp




