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



    def detectLoop(self):
        slow_p = self.head
        fast_p = self.head

        while slow_p and fast_p and fast_p.next:

            slow_p = slow_p.next
            fast_p = fast_p.next.next
            if slow_p == fast_p:
                print(slow_p.data,"  ",fast_p.data)
                return True
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
lList.head.next.next.next = lList.head.next

print(" is Linked List has Loop : ",lList.detectLoop())