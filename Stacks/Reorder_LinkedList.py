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
        while current is not None:
            print(current.data,end=" ")
            current = current.next


    def insertAtEnd(self,data):
        newNode = Node(data)
        current = self.head
        while current is not None and current.next is not None:
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
        while current is not None:
            stack.append(current.data)
            current = current.next
        current = head
        fromStack = False
        fromLinked = head
        list = LinkedList()
        while current is not None:
            if fromStack:
                list.insertAtEnd(stack.pop())
                fromStack = False
            else:
                list.insertAtEnd(fromLinked.data)
                fromStack = True
                fromLinked = fromLinked.next
            current =current.next
        list.printLinkedList()




lList = LinkedList()
lList.head = Node(1)
lList.insertAtEnd(2)
lList.insertAtEnd(3)
lList.insertAtEnd(4)
lList.insertAtEnd(5)
lList.insertAtEnd(6)
lList.insertAtEnd(7)
lList.insertAtEnd(8)
lList.insertAtEnd(9)
lList.insertAtEnd(10)
lList.reorderList(lList.head)




