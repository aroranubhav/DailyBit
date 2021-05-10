"""
    Problem 1347
    https://leetcode.com/problems/minimum-number-of-steps-to-make-two-strings-anagram/
    Date : 10/05/2021
"""

class Solution:
    def min_steps(self, s: str, t: str) -> int:
        if s == t:
            return 0

        char_list = [0] * 26
        for char in s:
            char_list[ord(char) - ord('a')] += 1

        for char in t:
            char_list[ord(char) - ord('a')] -= 1

        count = sum(filter(lambda x : x > 0, char_list))
        return count

"""
    Complexity : Time : O(n) | Space : O(1) 
"""