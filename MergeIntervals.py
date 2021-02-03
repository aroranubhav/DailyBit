"""
    Given an array of intervals where intervals[i] = [starti, endi],
    merge all overlapping intervals, and return an array of the non-overlapping intervals
    that cover all the intervals in the input.

    Example 1:
    Input: intervals = [[1,3],[2,6],[8,10],[15,18]]
    Output: [[1,6],[8,10],[15,18]]
    Explanation: Since intervals [1,3] and [2,6] overlaps, merge them into [1,6].

    Example 2:
    Input: intervals = [[1,4],[4,5]]
    Output: [[1,5]]
    Explanation: Intervals [1,4] and [4,5] are considered overlapping.
"""
class Solution:
    def merge_intervals(self, intervals: list[list[int]]) -> list[list[int]]:
        intervals = sorted(intervals, key=lambda x:x[0])
        ans = []
        start, end = intervals[0][0], intervals[0][1]

        for i in intervals:
            if i[0] > end:
                ans.append([start, end])
                start, end = i[0], i[1]
            else:
                end = max(end, i[1])

        ans.append([start, end])
        return ans

"""
    Complexity : Time : O(nlogn) | Space : O(n)
"""