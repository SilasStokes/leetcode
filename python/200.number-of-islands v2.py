#
# @lc app=leetcode id=200 lang=python3
#
# [200] Number of Islands
#
# https://leetcode.com/problems/number-of-islands/description/
#
# algorithms
# Medium (55.20%)
# Likes:    18748
# Dislikes: 419
# Total Accepted:    2.1M
# Total Submissions: 3.6M
# Testcase Example:  '[["1","1","1","1","0"],["1","1","0","1","0"],["1","1","0","0","0"],["0","0","0","0","0"]]'
#
# Given an m x n 2D binary grid grid which represents a map of '1's (land) and
# '0's (water), return the number of islands.
# 
# An island is surrounded by water and is formed by connecting adjacent lands
# horizontally or vertically. You may assume all four edges of the grid are all
# surrounded by water.
# 
# 
# Example 1:
# 
# 
# Input: grid = [
# ⁠ ["1","1","1","1","0"],
# ⁠ ["1","1","0","1","0"],
# ⁠ ["1","1","0","0","0"],
# ⁠ ["0","0","0","0","0"]
# ]
# Output: 1
# 
# 
# Example 2:
# 
# 
# Input: grid = [
# ⁠ ["1","1","0","0","0"],
# ⁠ ["1","1","0","0","0"],
# ⁠ ["0","0","1","0","0"],
# ⁠ ["0","0","0","1","1"]
# ]
# Output: 3
# 
# 
# 
# Constraints:
# 
# 
# m == grid.length
# n == grid[i].length
# 1 <= m, n <= 300
# grid[i][j] is '0' or '1'.
# 
# 
#

from ast import List
# @lc code=start
class Solution:
    # Input: grid = [
    #   ["2","1","1","1","0"],
    #   ["1","1","0","1","0"],
    #   ["1","1","0","0","0"],
    #   ["0","0","0","0","0"]
    # ]
    def numIslands(self, grid: List[List[str]]) -> int:


        LAND = "1"
        WATER = "0"
        count = 0
        EXPLORED = "3"
        #               right  left    up      down
        surrounding = [(1,0), (-1, 0), (0, 1), (0, -1)]
        to_explore = []
        # need to add all surrounding grid elements to a stack,
        # then call recursively on the stack
        # only add to the stack if its land
        def dfs(x: int, y:int):
            if grid[x][y] == WATER or grid == EXPLORED:
                return

            grid[x][y] = EXPLORED

            # if len(to_explore) == 0:
            #     count += 1

            for xx, yy in surrounding:
                xx = xx + x
                yy = yy + y
                if 0 <= xx < len(grid) and 0 <= yy < len(grid[xx]) and grid[xx][yy] == LAND:
                    dfs(xx, yy)
                    # to_explore.append((xx, yy))
            
            # while to_explore:
            #     xx, yy = to_explore.pop()
            #     dfs(xx, yy)
        
        for i in range(len(grid)):
            for j in range(len(grid[i])):
                if grid[i][j] == LAND:
                    count += 1
                    # grid[i][j] = EXPLORED
                    dfs(i, j)
        return count
        
# @lc code=end

