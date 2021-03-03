"""
    Given the head of a singly linked list,
    reverse the list, and return the reversed list.
"""
class ListNode:
     def __init__(self, val=0, next=None):
         self.val = val
         self.next = next

class Solution:
    def reverse(self, head: ListNode) -> ListNode:
        if not head:
            return None

        temp = None

        while head:
            n_node = head.next
            head.next = temp
            temp = head
            head = n_node

        return temp

"""
    Complexity : Time : O(n) | Space : O(1)
"""

