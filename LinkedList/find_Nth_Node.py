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

    def findNthNode(self,n):
        if self.head == None:
            print("List is empty")
            return
        current = self.head
        currentLoc = 1

        while currentLoc <= n:
            if currentLoc == n:
                print("Node at position %d :"%currentLoc,current.data)
                return
            if current.next == None:
                break
            current = current.next
            currentLoc += 1
        print("Incorrect Position")
        return



lList = LinkedList()
lList.head = Node(5)
a = Node(6)
b = Node(7)
lList.head.next = a
a.next = b
lList.insertAtEnd(9)

lList.printLinkedList()
lList.findNthNode(1)