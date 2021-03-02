"""
    Binary Search
"""
class Solution:
    def binary_search(self, nums: list[int], val: int) -> int:
        start_idx, end_idx = 0, len(nums) - 1

        while start_idx <= end_idx:
            mid = (start_idx + end_idx) // 2
            if nums[mid] == val:
                return mid
            elif nums[mid] < val:
                start_idx = mid + 1
            else:
                end_idx = mid - 1

        return -1

"""
    Complexity : Time : O(logn) | Space : O(1)
"""
