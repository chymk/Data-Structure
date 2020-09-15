class Node:
    def __init__(self,data=None):
        self.data = data
        self.next = None

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



    def findOccurence(self,current,key):
        if current == None:
            return self.count

        if current.data == key:
            self.count += 1

        return self.findOccurence(current.next,key)







lList = LinkedList()
lList.head = Node(5)
a = Node(6)
b = Node(7)
lList.head.next = a
a.next = b
lList.insertAtEnd(9)
lList.insertAtEnd(9)
lList.insertAtEnd(9)
lList.insertAtEnd(6)



lList.printLinkedList()
print(" Occurence of 6 : ",lList.findOccurence(lList.head,0))