#
# @lc app=leetcode id=200 lang=python3
#
# [200] Number of Islands
#
# https://leetcode.com/problems/number-of-islands/description/
# @lc code=start
class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:

        num_islands = 0
        height = len(grid)
        width = len(grid[0])
        visited = '#'
        offsets = [ (1,0), (-1,0), (0,1), (0, -1)]


        def dfs (row, column):
            if row < 0 or column < 0 or row >= len(grid) or column >= len(grid[0]) or grid[row][column] != '1':
                return
            grid[row][column] = visited
            for (y_off, x_off) in offsets:
                dfs(row + y_off, column + x_off)


        for row in range(len(grid)) :
            for column in range(len(grid[0])):
                if grid[row][column] == '1':
                    dfs(row, column)
                    num_islands += 1

        return num_islands

        
# @lc code=end


#
# algorithms
# Medium (54.05%)
# Likes:    15106
# Dislikes: 354
# Total Accepted:    1.7M
# Total Submissions: 3.1M
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
