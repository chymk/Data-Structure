class Node:
    def __init__(self,data=None):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

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

    def findCount(self):
        return self.getRecurCount(self.head)

    def getRecurCount(self,current):
        if current == None:
            return 0
        else:
            return 1 + self.getRecurCount(current.next)




lList = LinkedList()
lList.head = Node(5)
a = Node(6)
b = Node(7)
lList.head.next = a
a.next = b
lList.insertAtEnd(9)
lList.insertAtEnd(9)


lList.printLinkedList()
print("Linked List Length : ",lList.findCount())