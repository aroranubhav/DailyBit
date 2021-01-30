"""
    Given an array of strings strs, group the anagrams together.
    You can return the answer in any order.
    An Anagram is a word or phrase formed by rearranging the letters of a
    different word or phrase, typically using all the original letters exactly once.

    Example 1:

    Input: strs = ["eat","tea","tan","ate","nat","bat"]
    Output: [["bat"],["nat","tan"],["ate","eat","tea"]]
    Example 2:

    Input: strs = [""]
    Output: [[""]]
    Example 3:

    Input: strs = ["a"]
    Output: [["a"]]
"""
class Solution:
    def group_anagrams(self, strs: list[list[str]]) -> list[list[str]]:
        word_map = dict()

        for word in strs:
            sorted_word = "".join(sorted(word))
            if sorted_word in word_map:
                word_map[sorted_word].append(word)
            else:
                word_map[sorted_word] = [word]

        ans = []
        for value in word_map.values():
            ans.append(value)

        return ans

"""
    Complexity: Time : O(n) | Space : O(n)
"""


