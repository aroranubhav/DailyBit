class Solution:
    def sore_thumb(self, nums: list) -> int:
        iter_len = len(nums) - 1
        for i in range(1, iter_len):
            if nums[i - 1] < nums[i] > nums[i + 1]:
                return i

        return -1

sol = Solution()
arr = [1,2,3,7,4]
print(sol.sore_thumb(arr))


