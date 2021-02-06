"""
    Given an array nums and a value val, remove all instances of
    that value in-place and return the new length.

    Do not allocate extra space for another array, you must do
    this by modifying the input array in-place with O(1) extra memory.

    The order of elements can be changed. It doesn't matter
    what you leave beyond the new length.
"""
class Solution:
    def remove_element(self, nums: list[int], val: int) -> int:
        last_position = 0

        for num in nums:
            if num != val:
                nums[last_position] = num
                last_position += 1

        return last_position

"""
    Complexity: Time : O(n) | Space: O(1)
"""