class Node:
    def __init__(self, data=None):
        self.data = data
        self.next = None

class ClinkedList:
    def __init__(self):
        self.head = None

    def push(self, data):
        newNode = Node(data)
        current = self.head
        newNode.next = self.head

        if self.head is not None:
            while current.next != self.head:
                current = current.next
            current.next = newNode

        else:
            current = newNode
            current.next = current
            self.head = current

    def printLinkedList(self):
        current = self.head
        if self.head is not None:
            while True:
                print(current.data)
                current = current.next
                if(current == self.head):
                    break

    def splitLinkedList(self):
        head = self.head
        fast = head
        slow = head

        while fast.next is not head and fast is not head:
            slow = slow.next
            fast = fast.next
            fast = fast.next
        middle = slow.next
        slow.next = head
        fast.next = middle

        return



Clist = ClinkedList()
Clist.push(22)
Clist.push(25)
Clist.push(23)
Clist.push(27)
Clist.push(20)

#Clist.printLinkedList()

Clist.splitLinkedList()
Clist.printLinkedList()
