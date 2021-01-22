"""
    Given a reference to a binary search tree and a value to insert, return a reference
    to the root of the tree after the value has been inserted in a position that adheres
    to the invariants of a binary search tree.

    Ex:
    Input: root = [4,2,7,1,3], val = 5
    Output: [4,2,7,1,3,5]
"""
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:

    def insert(self, root: TreeNode, val: int) -> TreeNode:
        if not root:
            return TreeNode(val)

        if root.val > val:
            root.left = self.insert(root.left, val)

        else:
            root.right = self.insert(root.right, val)

        return root

"""
    Complexity : Time : O(n) | Space : O(n)
    n : number of nodes in the tree
"""

