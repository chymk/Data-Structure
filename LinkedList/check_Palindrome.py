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



    def is_Palindrome(self):
        stack = []
        current = self.head
        while current:
            stack.append(current.data)
            current = current.next
        current = self.head
        isPalind = False
        while current:
            i = stack.pop()

            if i == current.data :
                print(i,current.data)
                isPalind = True
            else:
                isPalind = False
                break
            current = current.next
        return isPalind


lList = LinkedList()
lList.head = Node(1)
#a = Node(2)
#b = Node(1)
'''lList.head.next = a
a.next = b
lList.insertAtEnd(4)
lList.insertAtEnd(3)
lList.insertAtEnd(2)
#lList.insertAtEnd(1)'''



lList.printLinkedList()

print("is Palindrome : ",lList.is_Palindrome())