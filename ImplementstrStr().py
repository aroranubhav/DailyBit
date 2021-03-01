"""
    Implement strStr().

    Return the index of the first occurrence of needle in haystack,
    or -1 if needle is not part of haystack.

    Clarification:

    What should we return when needle is an empty string?
    This is a great question to ask during an interview.

    For the purpose of this problem, we will return 0 when needle is an empty string.
    This is consistent to C's strstr() and Java's indexOf().

    Example 1:
    Input: haystack = "hello", needle = "ll"
    Output: 2

    Example 2:
    Input: haystack = "aaaaa", needle = "bba"
    Output: -1

    Example 3:
    Input: haystack = "", needle = ""
    Output: 0
"""
class Solution:
    def strstr(self, haystack: str, needle: str) -> int:
        if len(needle) == 0 or haystack == needle:
            return 0

        needle_len = len(needle)
        for idx in range(0, len(haystack) - needle_len + 1):
            sub_str = haystack[idx : idx + needle_len]
            if sub_str == needle:
                return idx

        return -1

"""
    Complexity : Time : O(n) | Space : O(1)
"""