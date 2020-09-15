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



    def detectLoop(self):
        s= set()
        current = self.head
        while current:
            if current in s:
                return True

            s.add(current)
            current = current.next

        return False


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
#lList.head.next.next.next = lList.head.next


#lList.printLinkedList()
print(" is Linked List has Loop : ",lList.detectLoop())