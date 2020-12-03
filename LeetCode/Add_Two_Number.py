# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def __init__(self):
        self.head = None

    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        carry = 0
        sum = 0
        temp = None

        while l1 is not None or l2 is not None:

            firstL = 0 if l1 is None else l1.val
            secondL = 0 if l2 is None else l2.val
            sum = carry + firstL + secondL
            carry = 0 if sum < 10 else 1
            sum = sum if sum < 10 else sum % 10
            temp = ListNode(sum)
            if self.head is None:
                self.head = temp
            else:
                prev.next = temp
            prev = temp

            if l1 is not None:
                l1 = l1.next
            if l2 is not None:
                l2 = l2.next
        if carry > 0:
            temp.next = ListNode(carry)
        return self.head

