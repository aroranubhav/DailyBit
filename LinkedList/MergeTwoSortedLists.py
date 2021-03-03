"""
    Merge two sorted linked lists and return it as a sorted list.
    The list should be made by splicing together the nodes
    of the first two lists.
"""
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def merge(self, l1: ListNode, l2: ListNode) -> ListNode:
        if not l1 and not l2:
            return None
        elif not l1:
            return l2
        elif not l2:
            return l1

        if l1.val < l2.val:
            temp = ListNode(l1.val)
            l1 = l1.next
        else:
            temp = ListNode(l2.val)
            l2 = l2.next

        head = temp

        while l1 and l2:
            if l1.val < l2.val:
                temp.next = ListNode(l1.val)
                l1 = l1.next
            else:
                temp.next = ListNode(l2.val)
                l2 = l2.next
            temp = temp.next

        if l1:
            temp.next = ListNode(l1.val, l1.next)

        if l2:
            temp.next = ListNode(l2.val, l2.next)

        return head

"""
    Complexity : Time: O(n) | Space : O(1)
"""