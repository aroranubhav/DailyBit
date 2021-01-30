"""
    We have a list of points on the plane.  Find the K closest points to the origin (0, 0).
    (Here, the distance between two points on a plane is the Euclidean distance.)
    You may return the answer in any order.
    The answer is guaranteed to be unique (except for the order that it is in.)

    Input: points = [[1,3],[-2,2]], K = 1
    Output: [[-2,2]]
    Explanation:
    The distance between (1, 3) and the origin is sqrt(10).
    The distance between (-2, 2) and the origin is sqrt(8).
    Since sqrt(8) < sqrt(10), (-2, 2) is closer to the origin.
    We only want the closest K = 1 points from the origin, so the answer is just [[-2,2]].
"""
import heapq
class Solution:
    def kClosest(self, points: list[list[int]], k: int) -> list[list[int]]:
        result = []

        for point in points:
            curr_dist = pow((point[0] ** 2 + point[1] ** 2),0.5)
            result.append([curr_dist, point])

        return [x[1] for x in sorted(result)][0:k]

    #solution using max-heap
    def k_closest(self, points: list[list[int]], k: int) -> list[list[int]]:
        heap = []

        for point in points:
            if len(heap) < k:
                heapq.heappush(heap, (self.euclidean_dist(point), point))
            else:
                heapq.heappushpop(heap, (self.euclidean_dist(point), point))

        ans = []
        for point in heap:
            ans.append(point[1])

        return ans

    def euclidean_dist(self, point) -> int:
        return pow((point[0] ** 2 + point[1] ** 2), 0.5)


"""
    Complexity : Time : O(nlogn) | Space : O(n)
"""

