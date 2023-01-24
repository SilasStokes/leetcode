#
# @lc app=leetcode id=74 lang=python3
#
# [74] Search a 2D Matrix
#
# https://leetcode.com/problems/search-a-2d-matrix/description/
#
# algorithms
# Medium (46.15%)
# Likes:    10436
# Dislikes: 316
# Total Accepted:    1M
# Total Submissions: 2.2M
# Testcase Example:  '[[1,3,5,7],[10,11,16,20],[23,30,34,60]]\n3'
#
# Write an efficient algorithm that searches for a value target in an m x n
# integer matrix matrix. This matrix has the following properties:
# 
# 
# Integers in each row are sorted from left to right.
# The first integer of each row is greater than the last integer of the
# previous row.
# 
# 
# 
# Example 1:
# 
# 
# Input: matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]], target = 3
# Output: true
# 
# 
# Example 2:
# 
# 
# Input: matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]], target = 13
# Output: false
# 
# 
# 
# Constraints:
# 
# 
# m == matrix.length
# n == matrix[i].length
# 1 <= m, n <= 100
# -10^4 <= matrix[i][j], target <= 10^4
# 
# 
#

# @lc code=start
from typing import List


class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        if not matrix or target < matrix[0][0] or target > matrix[-1][-1]:
            return False


        m, n = len(matrix), len(matrix[0])

        # binary search for the right row. 
        l, r = 0, m - 1
        row = -1
        while l <= r:
            row = (r - l )//2 + l
            if matrix[ row ][0] <= target <= matrix[ row ][-1]:
                break
            elif target < matrix[row][0]:
                r = row - 1
            else:
                l = row + 1
        # now we have row, find it in row using binary search
        l, r = 0, n - 1
        while l <= r:
            index = (r - l ) // 2 + l
            val = matrix[row][index]
            if val == target:
                return True
            elif target < val:
                r = index - 1
            else:
                l = index + 1

        return False



        # for i in range(m):

        
# @lc code=end

