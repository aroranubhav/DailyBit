"""
    Given an integer n, return whether or not it is a “magical” number.
    A magical number is an integer such that when you
    repeatedly replace the number with the sum of the
    squares of its digits its eventually becomes one.

    Ex: Given the following integer n…

    n = 44, return true.
    4^2 + 4^2 = 32
    3^2 + 2^2 = 13
    1^2 + 3^2 = 10
    1^2 + 0^2 = 1.
"""
class Solution:

    def magic_number(self, n: int) -> bool:
        while n != 1:
            d_sum = 0
            while n != 0:
                d_sum += (n % 10) * (n % 10)
                n = n // 10

            print(d_sum)
            if d_sum > 10:
                n = d_sum
            else:
                return d_sum == 1 or d_sum == 10

        return False

sol = Solution()
print(sol.magic_number(44))
