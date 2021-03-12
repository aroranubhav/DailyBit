"""
    Given the head of a sorted linked list, remove the duplicate
    nodes from the list and return its head.
    The linked list should be modified in place.
"""
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def remove_duplicates(self, head: ListNode) -> ListNode:
        curr_node = head

        while curr_node and curr_node.next:
            if curr_node.val == curr_node.next.val:
                curr_node.next = curr_node.next.next
            else:
                curr_node = curr_node.next

        return head

"""
    Complexity : Time : O(n) | Space : O(1)
"""