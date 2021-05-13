"""
    Problem 451
    https://leetcode.com/problems/sort-characters-by-frequency/
    Date : 12/05/2021
"""


class Solution:
    def frequency_sort(self, s: str) -> str:
        char_map = dict()

        for char in s:
            char_map[char] = char_map.get(char, 0) + 1

        char_map = dict(sorted(char_map.items(), key = lambda x: x[1], reverse= True))

        ans = ''
        for key, value in char_map.items():
            ans += key * value

        return ans

"""
    Complexity : Time: O(nlogn) | Space: O(n)
"""
