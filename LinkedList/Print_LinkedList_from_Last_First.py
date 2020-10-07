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

    def printReverse(self,list):
        if list == None:
            return
        head = list
        tail =  head.next
        self.printReverse(tail)
        print(head.data)





lList = LinkedList()
lList.head = Node(1)
a = Node(2)
b = Node(3)
lList.head.next = a
a.next = b
lList.insertAtEnd(4)
lList.insertAtEnd(5)
lList.insertAtEnd(6)
lList.insertAtEnd(7)
lList.insertAtEnd(8)
lList.insertAtEnd(9)
lList.insertAtEnd(10)

lList.printLinkedList()
print("reverse")
lList.printReverse(lList.head)


