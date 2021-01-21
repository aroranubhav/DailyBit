"""
    Given two linked lists that represent two numbers, return the sum of the numbers also represented as a list.

    Ex: Given the two linked list
    a = 3->2, b = 1->5, return a list that looks as follows: 4->6

    Ex: Given the two linked lists
    a = 2->4->3, b = 5->6->4, return a list that looks as follows: 7->0->8
"""

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode):
        if not l1 and not l2:
            return None

        sumList = ListNode(0)
        curr = sumList
        carry = 0

        while l1 or l2:
            x = l1.val if l1 else 0
            y = l2.val if l2 else 0

            curr_sum = x + y + carry
            carry = curr_sum // 10
            curr.next = ListNode(curr_sum % 10)
            curr = curr.next

            if l1:
                l1 = l1.next
            if l2:
                l2 = l2.next

        if carry > 0:
            curr.next = ListNode(carry)

        return sumList.next

"""
    Complexity : Time : O(max(m, n) | Space : O(max(m, n))
    m : length of l1
    n : length of l2
"""

