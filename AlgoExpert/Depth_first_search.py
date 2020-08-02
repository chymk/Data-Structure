'''You are given a Node class that has a name and an array of optional children Nodes. When put together, Nodes form a simple tree-like structure. Implement the
depthFirstSearch method on the Node class, which takes in an empty array, traverses the tree using the Depth-rst Search approach (specically navigating the
tree from left to right), stores all the of the Nodes' names in the input array, and returns it.

Sample input:
         A
       / | \
      B  C  D
     / \   / \
    E   F G   H
       / \ \
      I  J  K
Sample output: ["A","B","E","F","I","J","C","D","G","K","H"]'''


class node:
    def __init__(self, name):
        self.child = []
        self.name = name

    def add_child(self,name):
        self.child.append(node(name))
        return self

    def depth_first_search(self,array=[]):
        array.append(self.name)
        for child in self.child:
            child.depth_first_search(array)
        return array

test1 = node('A')
test1.add_child('B').add_child('C').add_child('D')
test1.child[0].add_child('E').add_child('F')
test1.child[2].add_child('G').add_child('H')
test1.child[0].child[1].add_child('I').add_child('J')
test1.child[2].child[0].add_child('K')

print(test1.depth_first_search())


test2 = node("A")
test2.add_child("B").add_child("C").add_child("D").add_child("E")
test2.child[1].add_child("F")
print(test2.depth_first_search())
