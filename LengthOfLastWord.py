"""
    Given a string s consists of some words separated by spaces,
    return the length of the last word in the string.
    If the last word does not exist, return 0.
    A word is a maximal substring consisting of non-space characters only.

    Example 1:
    Input: s = "Hello World"
    Output: 5

    Example 2:
    Input: s = " "
    Output: 0
"""
class Solution:
    def last_word_length(self, s: str) -> int:
        word_len = 0
        s = s.strip()
        for i in range(len(s) - 1, -1, -1):
            if s[i] == ' ':
                break
            word_len += 1

        return word_len

sol = Solution()
print(sol.last_word_length("  "))

"""
    Complexity: Time : O(n) | Space : O(1)
"""
