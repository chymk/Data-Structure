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
        while current.next is not None:
            current = current.next
        if self.head is None:
            self.head = newNode
        else:
            current.next = newNode
            newNode.next = None


    def reorderList(self,head):
        if head is None:
            return None
        current = head
        stack = [-1]
        while current.next is not None:
            stack.append(current.data)
            current = current.next
        current = head
        fromStack = True
        fromLinked = head
        list = LinkedList()
        while current.next is not None:
            if fromStack:
                list.insertAtEnd(stack.pop())
                fromStack = False
            else:
                list.insertAtEnd(fromLinked)
                fromStack = True
                fromLinked = fromLinked.next
            current =current.next
        list.printLinkedList()




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
lList.reorderList(lList.head)




