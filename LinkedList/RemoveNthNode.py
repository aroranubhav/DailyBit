"""
    Given the head of a linked list, remove the nth
    node from the end of the list and return its head.
"""
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def remove_nth_from_end(self, head : ListNode, n : int) -> ListNode:
        slow_ptr = fast_ptr = head

        for i in range(n):
            fast_ptr = fast_ptr.next

        if not fast_ptr:
            return head.next

        while fast_ptr.next:
            fast_ptr = fast_ptr.next
            slow_ptr = slow_ptr.next

        slow_ptr.next = slow_ptr.next.next

        return head

"""
    Complexity : Time : O(n) | Space : O(1)
"""