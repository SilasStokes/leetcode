#
# @lc app=leetcode id=973 lang=python3
#
# [973] K Closest Points to Origin
#
import heapq
# Accepted
# 87/87 cases passed (1307 ms)
# Your runtime beats 36.4 % of python3 submissions
# Your memory usage beats 59.09 % of python3 submissions (20.3 MB)

# @lc code=start
class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        heap = []
        for (x, y ) in points:
            dist = -(x*x + y*y)

            if len(heap) == k:
                heapq.heappushpop(heap, (dist, x ,y))
            else:
                heapq.heappush(heap, (dist, x , y))
        return [ (x, y) for (dist, x, y) in heap ]



        
# @lc code=end

# class Solution:
#     def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
#         index_dist = []
#         for i, (x, y) in enumerate(points):
#             dist = math.sqrt( x**2 + y**2)
#             index_dist.append((i, dist))

#         sorted_indexes = sorted(index_dist, key=lambda t: t[1]) # n log n

#         return_val = []
#         for i in range(k):
#             return_val.append( points[sorted_indexes[i][0]] )

#         return return_val
