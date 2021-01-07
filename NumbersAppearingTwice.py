"""
    Given an array of integers, nums, each element in the
    array either appears once or twice. Return a list containing all
    the numbers that appear twice.
    Note: Each element in nums is between one and nums.length (inclusive).

    Ex: Given the following array nums…
    nums = [9, 3, 7, 6, 9], return [9].

    Ex: Given the following array nums…
    nums = [3, 2, 8], return [].

    Ex: Given the following array nums…
    nums = [7, 1, 1, 7, 3, 4, 4], return [7,1,4].
"""

class Solution:

    def repeating_numbers(self, nums: list) -> list:
        r_nums = []
        num_map = dict()
        for num in nums:
            if num in num_map:
                num_map[num] = 2
            else:
                num_map[num] = 1

        for key, val in num_map.items():
            if val == 2:
                r_nums.append(key)

        return r_nums

arr = [9, 3, 7, 6, 9]
sol = Solution()
ans = sol.repeating_numbers(arr)

for value in ans:
    print(value, end = ' ')

"""
    Complexity : Time : O(n) | Space : O(n)
"""