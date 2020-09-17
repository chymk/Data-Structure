class Node:
    def __init__(self,data=None):
        self.data = data
        self.next = None
        self.flag = False

class LinkedList:
    def __init__(self):
        self.head = None
        self.count = 0


    def printLinkedList(self):
        current = self.head
        while current != None:
            print(current.data)
            current = current.next


    def insertAtEnd(self,data):
        newNode = Node(data)
        current = self.head
        while current.next != None:
            current = current.next
        if self.head == None:
            self.head = newNode
        else:
            current.next = newNode
            newNode.next = None

    def removeDuplicates(self):
        s = set()
        current = self.head
        prev = None
        while current is not None:
            if current.data in set:
                if current == self.head:
                    self.head = current.next
                elif current.next is None:
                    prev.next = None
                else:
                    prev.next = current.next
            s.add(current.data)
            prev = current
            current = current.next
        return



lList = LinkedList()
lList.head = Node(5)
a = Node(6)
b = Node(7)
lList.head.next = a
a.next = b
lList.insertAtEnd(9)
lList.insertAtEnd(2)
lList.insertAtEnd(1)
lList.insertAtEnd(0)
lList.insertAtEnd(0)
lList.insertAtEnd(3)
lList.insertAtEnd(4)

lList.printLinkedList()
lList.removeDuplicates()
lList.printLinkedList()
