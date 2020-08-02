'''
Write a class for a Doubly Linked List. The class should have a "head" and "tail" properties, both of which should point to either the None (null) value or to a
Linked List node. Every node will have a "value" property as well as "next" and "prev" properties, both of which can point to either the None (null) value or
another node. The class should support setting the head and tail of the linked list, inserting nodes before and after other nodes as well as at certain positions,
removing given nodes and removing nodes with specic values, and searching for nodes with values. Only the searching method should return a value:
specically, a boolean.

Sample input:
1 -> 2 -> 3 -> 4 -> 5
Sample output (after setting 4 to head):
4 -> 1 -> 2 -> 3 -> 5
Sample output (after setting 6 to tail):
4 -> 1 -> 2 -> 3 -> 5 -> 6
Sample output (after inserting 3 before 6):
4 -> 1 -> 2 -> 5 -> 3 -> 6
Sample output (after inserting a new 3 after 6):
4 -> 1 -> 2 -> 5 -> 3 -> 6 -> 3
Sample output (after inserting a new 3 at position 1):
3 -> 4 -> 1 -> 2 -> 5 -> 3 -> 6 -> 3
Sample output (after removing nodes with value 3):
4 -> 1 -> 2 -> 5 -> 6
Sample output (after removing 2):
4 -> 1 -> 5 -> 6
Sample output (after searching for 5): True'''

# This is an input class. Do not edit. class Node:    def __init__(self, value):        self.value = value        self.prev = None        self.next = None
# Feel free to add new properties and methods to the class. class DoublyLinkedList:    def __init__(self):        self.head = None        self.tail = None
    def setHead(self, node):        # Write your code here.        pass
    def setTail(self, node):        # Write your code here.        pass
    def insertBefore(self, node, nodeToInsert):        # Write your code here.        pass
    def insertAfter(self, node, nodeToInsert):        # Write your code here.        pass
    def insertAtPosition(self, position, nodeToInsert):        # Write your code here.        pass
    def removeNodesWithValue(self, value):        # Write your code here.        pass
    def remove(self, node):        # Write your code here.        pass
    def containsNodeWithValue(self, value):        # Write your code here.        pass
