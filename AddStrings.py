"""
    Given two non-negative integers num1 and num2 represented as string,
    return the sum of num1 and num2.

    Note:
    The length of both num1 and num2 is < 5100.
    Both num1 and num2 contains only digits 0-9.
    Both num1 and num2 does not contain any leading zero.
    You must not use any built-in BigInteger library or convert the inputs to integer directly.
"""
class Solution:
    def add_strings(self, num1: str, num2: str) -> str:
        def convert(c):
            return ord(c) - ord('0')

        x1=x2=0
        for i in num1:
            x1 = x1 * 10 + convert(i)

        for i in num2:
            x2 = x2 * 10 + convert(i)

        return str(x1 + x2)

"""
    Complexity : Time : O(n) | Space : O(1)
"""