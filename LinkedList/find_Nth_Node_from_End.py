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

    def findNthNodefromEnd(self,n):
        if self.head == None:
            print("List is empty")
            return
        current = self.head
        NthNode = self.head
        currentLoc = 1

        while current != None:
            if currentLoc > n:
                NthNode = NthNode.next
            if current.next == None:
                break
            current = current.next
            currentLoc += 1
        if(n>currentLoc):
            print("Invaid Location")
            return
        print("NthNodeFromEnd ",NthNode.data)
        return


lList = LinkedList()
lList.head = Node(5)
a = Node(6)
b = Node(7)
lList.head.next = a
a.next = b
lList.insertAtEnd(9)

lList.printLinkedList()
lList.findNthNodefromEnd(1)
