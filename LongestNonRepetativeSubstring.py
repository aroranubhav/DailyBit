"""
    Given a string s, find the length of the longest substring without repeating characters.

    Ex: Given the following string s
    s = "ababbc", return 2.

    Ex: Given the following string s
    s = "pppp", return 1.

    Ex: Given the following string s
    s = "abcdeed", return 5.
"""


class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        u_list = set()
        i = j = max_len = 0

        while j < len(s):
            if s[j] not in u_list:
                u_list.add(s[j])
                j += 1
                max_len = max(max_len, j - i)
            else:
                u_list.remove(s[i])
                i += 1

        return max_len


"""
    Complexity : Time : O(n) | Space : O(n)
"""