"""
    Problem 1347
    https://leetcode.com/problems/minimum-number-of-steps-to-make-two-strings-anagram/
    Date : 10/05/2021
"""
class Solution:
    def add_one(self, digits: list[int]) -> list[int]:
        for i in range(len(digits) - 1, -1, -1):
            if i == 0 and digits[i] == 9:
                digits[i] = 0
                digits.insert(0, 1)
            elif digits[i] == 9:
                digits[i] = 0
            else:
                digits[i] += 1
                break

        return digits

"""
    Complexity : Time : O(n) | Space : O(1)
"""