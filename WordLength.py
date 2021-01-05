"""
   Problem : Given a string, s, return the length of the last word.
   Eg: "The is a string"
   return 5, as string is 5 characters long
"""

class Solution:
    def __init__(self, string: str):
        self.string = string

    """
       Complexity : Time : O(n) | Space : O(n)
    """

    def word_length_1(self) -> int:
        length = 0
        for char in reversed(self.string.strip()):
            if char == ' ':
                return length
            else:
                length += 1

    """
       Complexity : Time : O(n) | Space : O(1)
    """

    def word_length(self) -> int:
        length = 0
        trailingspace = 0

        for char in reversed(self.string):
            if char == ' ':
                trailingspace += 1
            else:
                break

        start_idx = len(self.string) - trailingspace - 1

        for idx in range(start_idx, 0, -1):
            if self.string[idx] == ' ':
                return length
            else:
                length += 1

        return len(self.string) - trailingspace

wordlen = Solution(input("Enter the string: "))
print(wordlen.word_length())






