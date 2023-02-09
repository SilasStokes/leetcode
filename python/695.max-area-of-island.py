#
# @lc app=leetcode id=695 lang=python3
#
# [695] Max Area of Island
#
# https://leetcode.com/problems/max-area-of-island/description/
#
# algorithms
# Medium (71.46%)
# Likes:    8571
# Dislikes: 192
# Total Accepted:    675.4K
# Total Submissions: 941.1K
# Testcase Example:  '[[0,0,1,0,0,0,0,1,0,0,0,0,0],[0,0,0,0,0,0,0,1,1,1,0,0,0],[0,1,1,0,1,0,0,0,0,0,0,0,0],[0,1,0,0,1,1,0,0,1,0,1,0,0],[0,1,0,0,1,1,0,0,1,1,1,0,0],[0,0,0,0,0,0,0,0,0,0,1,0,0],[0,0,0,0,0,0,0,1,1,1,0,0,0],[0,0,0,0,0,0,0,1,1,0,0,0,0]]'
#
# You are given an m x n binary matrix grid. An island is a group of 1's
# (representing land) connected 4-directionally (horizontal or vertical.) You
# may assume all four edges of the grid are surrounded by water.
# 
# The area of an island is the number of cells with a value 1 in the island.
# 
# Return the maximum area of an island in grid. If there is no island, return
# 0.
# 
# 
# Example 1:
# 
# 
# Input: grid =
# [[0,0,1,0,0,0,0,1,0,0,0,0,0],[0,0,0,0,0,0,0,1,1,1,0,0,0],[0,1,1,0,1,0,0,0,0,0,0,0,0],[0,1,0,0,1,1,0,0,1,0,1,0,0],[0,1,0,0,1,1,0,0,1,1,1,0,0],[0,0,0,0,0,0,0,0,0,0,1,0,0],[0,0,0,0,0,0,0,1,1,1,0,0,0],[0,0,0,0,0,0,0,1,1,0,0,0,0]]
# Output: 6
# Explanation: The answer is not 11, because the island must be connected
# 4-directionally.
# 
# 
# Example 2:
# 
# 
# Input: grid = [[0,0,0,0,0,0,0,0]]
# Output: 0
# 
# 
# 
# Constraints:
# 
# 
# m == grid.length
# n == grid[i].length
# 1 <= m, n <= 50
# grid[i][j] is either 0 or 1.
# 
# 
#

from ast import List

# @lc code=start
class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        ROWS, COLS = len(grid), len(grid[0])
        visit = set()

        def dfs(r, c):
            if (
                r < 0
                or r == ROWS
                or c < 0
                or c == COLS
                or grid[r][c] == 0
                or (r, c) in visit
            ):
                return 0
            visit.add((r, c))
            return 1 + dfs(r + 1, c) + dfs(r - 1, c) + dfs(r, c + 1) + dfs(r, c - 1)

        area = 0
        for r in range(ROWS):
            for c in range(COLS):
                area = max(area, dfs(r, c))
        return area
        
# @lc code=end
#  0 1 2 3 4 5 6 7 8 9 0 1 2 
#0[0,0,1,0,0,0,0,1,0,0,0,0,0],
#1[0,0,0,0,0,0,0,1,1,1,0,0,0],
#2[0,1,1,0,1,0,0,0,0,0,0,0,0],
#3[0,1,0,0,1,1,0,0,1,0,1,0,0],
#4[0,1,0,0,1,1,0,0,1,1,1,0,0],
#5[0,0,0,0,0,0,0,0,0,0,1,0,0],
#6[0,0,0,0,0,0,0,1,1,1,0,0,0],
#7[0,0,0,0,0,0,0,1,1,0,0,0,0]
# winner: (3, 8), (4, 8), (4, 9), (4, 10), (3, 10), (5, 10)

    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        WATER, LAND, EXPLORED = 0, 1, 2
        #                     down  up     right     left
        surrounding_tiles = [(1,0), (-1, 0), (0, 1), (0, -1)]
        max_area = 0
        area = 0
        def search(r:int, c:int) -> None: # row, column
            nonlocal max_area, area 
            if (not 0 <= r < len(grid) or \
                not 0 <= c < len(grid[r]) or \
                grid[r][c] == WATER or \
                grid[r][c] == EXPLORED
               ):
                return
            area += 1
            max_area = max(max_area, area)
            grid[r][c] = EXPLORED
            for rr, cc in surrounding_tiles:
                rr, cc = r + rr, c + cc
                search(rr, cc)

        for x in range(len(grid)):
            for y in range(len(grid[x])):
                area = 0
                search(x, y)
        return max_area
