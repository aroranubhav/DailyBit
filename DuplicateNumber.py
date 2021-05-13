"""
    Problem 287
    https://leetcode.com/problems/find-the-duplicate-number/
    Date : 11/05/2021
"""


class Solution:
    def find_duplicate(self, nums: list[int]) -> int:
        if len(nums) > 1:
            slow = nums[0]
            fast = nums[nums[0]]

            while slow != fast:
                slow = nums[0]
                fast = nums[nums[0]]

            fast = 0

            while slow != fast:
                slow = nums[slow]
                fast = nums[fast]

            return slow

        return -1

"""
    Complexity : Time : O(n) | Space : O(1) 
"""

