"""
    Given an array nums, return the third largest (distinct) value.
    Note: If the third largest number does not exist, return the largest value.

    Ex: Given the following array nums…
    nums = [1, 9, 2, 4, 6], return 4.

    Ex: Given the following array nums…
    nums = [1, 8, 6, 8], return 1.

    Ex: Given the following array nums…
    nums = [5, 11], return 11.
"""

import heapq
class Solution:

    def findkthlargest(self, nums: list, k: int) -> int:
        heap = []
        heapq.heapify(heap)

        for num in nums:
            if len(heap) < k:
                heapq.heappush(heap, num)
            elif num > heap[0] and num not in heap:
                heapq.heappop(heap)
                heapq.heappush(heap, num)

        if len(heap) < k:
            return max(heap)

        return heap[0]

kthlargest = Solution()
print(kthlargest.findkthlargest([3,4,10,1], 2))

"""
    Complexity : Time : O(n + klog(n)) | Space : O(n)
"""



