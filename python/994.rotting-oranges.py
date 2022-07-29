#
# @lc app=leetcode id=994 lang=python3
# @lc code=start
import copy
class Solution:
    # [2,1,1],
    # [0,1,1],
    # [1,0,1]
    def orangesRotting(self, grid: List[List[int]]) -> int:
        if not grid: return -1

        height = len(grid)
        width = len(grid[0])

        fresh = 0

        rotten = []

        for r in range(height):
            for c in range(width):
                if grid[r][c] == 1:
                    fresh += 1
                if grid[r][c] == 2:
                    rotten.insert(0, (r,c) )

        minutes = 0

        while rotten and fresh > 0 :
            minutes += 1

            for _ in range(len(rotten)):
                r, c = rotten.pop()

                for row, col in [ (r + 1, c), (r - 1, c), (r, c + 1), (r, c -1) ]:
                    if row < 0 or col < 0 or row >= height or col >= width:
                        continue

                    if grid[row][col] == 0 or grid[row][col] == 2:
                        continue

                    fresh -= 1

                    grid[row][col] = 2

                    rotten.insert(0, (row, col))

        return minutes if fresh == 0 else -1








        
# @lc code=end

#     def orangesRotting(self, grid: List[List[int]]) -> int:
#         if not grid: return -1

#         height = len(grid)
#         width = len(grid[0])

#         # if no fresh oranges return 0
#         flag = [] 
#         for row in grid:
#             if 1 not in row:



                

#         minutes = []

#         q = []



#         for r in range(height):
#             for c in range(width):
#                 if grid[r][c] == 2: # we have a rotten orange, do bfs
#                     q.append( (r, c))
#                     local_minutes = -1
#                     level = 1
#                     nxt_level = 0
#                     local_grid = copy.deepcopy(grid)

#                     while q:
#                         row, col = q.pop()
#                         level -= 1
                        
#                         # bfs
#                         if row - 1 >= 0 and local_grid[row - 1][col] == 1:
#                             local_grid[row - 1][col] = -1
#                             nxt_level += 1
#                             q.insert(0, (row-1, col))

#                         if row + 1 < height and local_grid[row +1][col] == 1:
#                             local_grid[row+1][col] = -1
#                             nxt_level += 1
#                             q.insert(0, (row+1, col))
                        
#                         if col - 1 >= 0 and local_grid[row][col - 1] == 1:
#                             local_grid[row][col-1] = -1
#                             nxt_level += 1
#                             q.insert(0, (row, col -1))

#                         if col + 1 < width and local_grid[row][col + 1] == 1:
#                             local_grid[row][col + 1] = -1
#                             nxt_level += 1
#                             q.insert(0, (row, col +1))

#                         if level == 0:
#                             local_minutes += 1

#                             level = nxt_level
#                             nxt_level = 0
                    
#                     flag = False
#                     for row in local_grid:
#                         if 1 in row:
#                             flag = True
#                             minutes.append(-1)
#                     if not flag:
#                         minutes.append(local_minutes)

#         minutes.sort()
#         return minutes[0] if minutes else 
# #
# [994] Rotting Oranges
#
# https://leetcode.com/problems/rotting-oranges/description/
#
# algorithms
# Medium (51.76%)
# Likes:    7472
# Dislikes: 286
# Total Accepted:    435.9K
# Total Submissions: 837.4K
# Testcase Example:  '[[2,1,1],[1,1,0],[0,1,1]]'
#
# You are given an m x n grid where each cell can have one of three
# values:
# 
# 
# 0 representing an empty cell,
# 1 representing a fresh orange, or
# 2 representing a rotten orange.
# 
# 
# Every minute, any fresh orange that is 4-directionally adjacent to a rotten
# orange becomes rotten.
# 
# Return the minimum number of minutes that must elapse until no cell has a
# fresh orange. If this is impossible, return -1.
# 
# 
# Example 1:
# 
# 
# Input: grid = [[2,1,1],[1,1,0],[0,1,1]]
# Output: 4
# 
# 
# Example 2:
# 
# 
# Input: grid = [[2,1,1],[0,1,1],[1,0,1]]
# Output: -1
# Explanation: The orange in the bottom left corner (row 2, column 0) is never
# rotten, because rotting only happens 4-directionally.
# 
# 
# Example 3:
# 
# 
# Input: grid = [[0,2]]
# Output: 0
# Explanation: Since there are already no fresh oranges at minute 0, the answer
# is just 0.
# 
# 
# 
# Constraints:
# 
# 
# m == grid.length
# n == grid[i].length
# 1 <= m, n <= 10
# grid[i][j] is 0, 1, or 2.
# 
# 
#
