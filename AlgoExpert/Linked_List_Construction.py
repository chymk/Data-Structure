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

class Node:
    def __init__(self, value):
        self.value = value
        self.prev = None
        self.next = None

# Feel free to add new properties and methods to the class.
class DoublyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def setHead(self, node):
        if self.head is None:
            self.head = node
            self.tail = node
            return
        else:
            self.insertBefore(self.head,node)
        return


    def setTail(self, node):
        if self.tail is None:
            self.setHead(node)
            return
        else:
            self.insertAfter(self.tail,node)

    def insertBefore(self, node, nodeToInsert):
        prevNode = node.prev
        prevNode.next = nodeToInsert
        nodeToInsert.next = node
        nodeToInsert.prev =prevNode
        node.prev = nodeToInsert
        return

    def insertAfter(self, node, nodeToInsert):
        nextNode = node.next
        node.next =nodeToInsert
        nodeToInsert.prev = node
        nodeToInsert.next = nextNode
        return

    def insertAtPosition(self, position, nodeToInsert):
        location = 0
        iterateNode = self.head
        while iterateNode.next and location > position:
            if location == position:
                self.insertBefore(iterateNode,nodeToInsert)
                return
        return

    def removeNodesWithValue(self, value):
        iterateNode = self.head
        while iterateNode.next:
            if iterateNode.value == value:
                self.remove(iterateNode)
                return
        return
        pass

    def remove(self, node):
        prevNode = node.prev
        nextNode = node.next
        prevNode.next = nextNode
        nextNode.prev = prevNode
        pass

    def containsNodeWithValue(self, value):
        iterateNode =self.head
        while iterateNode.next:
            if iterateNode.value == value:
                return True
        return False