"""
    Given a string s containing just the characters '(', ')', '{', '}', '[' and ']',
    determine if the input string is valid.
    An input string is valid if:
    Open brackets must be closed by the same type of brackets.
    Open brackets must be closed in the correct order.


    Example 1:
    Input: s = "()"
    Output: true

    Example 2:
    Input: s = "()[]{}"
    Output: true

    Example 3:
    Input: s = "(]"
    Output: false

    Example 4:
    Input: s = "([)]"
    Output: false

    Example 5:
    Input: s = "{[]}"
    Output: true
"""

class Solution:
    def valid_parentheses(self, s: str) -> bool:
        stack = []
        opening_braces, closing_braces = "({[", ")}]"

        for char in s:
            if char in opening_braces:
                stack.append(char)
            elif char in closing_braces and len(stack) == 0:
                return False
            elif char == ')' and stack[-1] == '(' or char == '}' and stack[-1] == '{' or char == ']' and stack[-1] == '[':
                stack.pop()
            else:
                return False

        return len(stack) == 0

"""
    Complexity : Time : O(n) | Space : O(n)
"""
