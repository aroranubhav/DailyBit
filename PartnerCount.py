"""
    Given an integer array, nums, return the total number of “partners” in the array.
    Note: Two numbers in our array are partners if they reside at different indices and both contain the same value.

    Ex: Given the following array nums…
    nums = [4, 5, 5, 1, 4, 4, 1], return 5.
    5 (index 1) and 5 (index 2) are partners.
    1 (index 3) and 1 (index 6) are partners.
    4 (index 0) and 4 (index 4) are partners.
    4 (index 0) and 4 (index 5) are partners.
    4 (index 4) and 4 (index 5) are partners.

"""
class Solution:
    def partners(self, arr: list) -> int:
        list_map = {}
        partner_count = 0

        for value in arr:
            if value in list_map:
                list_map[value] = list_map[value] + 1
            else:
                list_map[value] = 1

        for key, value in list_map.items():
            if value > 1:
                partner_count += self.factorial(value)

        return partner_count

    def factorial(self, n):
        res = 1

        for i in range(2, n + 1):
            res = res * i

        return res
"""
    Complexity : Time : O(n) | Space : O(n)
"""