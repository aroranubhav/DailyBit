"""
    Given an integer array, sorted in ascending order and a target value,
    return two unique indices (one based) such that the values at those
    indices sum to the given target value.

    Example 1:
    Input: nums = [2,7,11,15], target = 9
    Output: [1,2]
    Output: Because nums[0] + nums[1] == 9, we return [1, 2].

    Example 2:
    Input: nums = [3,3], target = 6
    Output: [1,2]
"""
class Solution:
    def sumpair(self, nums: list[int], target: int) -> list[int]:
        start, end = 0, len(nums) - 1

        while start < end:
            curr_sum = nums[start] + nums[end]
            if curr_sum == target:
                return [start + 1, end + 1]
            elif curr_sum > target:
                end -= 1
            else:
                start += 1

        return []

"""
    Complexity : Time : O(n) | Space : O(1)
"""