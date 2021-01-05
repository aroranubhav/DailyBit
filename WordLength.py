"""Problem : Given a string, s, return the length of the last word.
   Eg: "The is a string"
   return 5, as string is 5 characters long
"""
class Solution:
    def __init__(self, string: str):
        self.string = string

    def word_length(self) -> int:
        length = 0
        for char in reversed(self.string.strip()):
            if char == ' ':
                return length
            else:
                length += 1

wordlen = Solution(input("Enter the string: "))
print(wordlen.word_length())





