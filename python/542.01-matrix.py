#
# @lc app=leetcode id=542 lang=python3
#
# [542] 01 Matrix
#

# @lc code=start

class Solution:
# Runtime: 1112 ms, faster than 37.77% of Python3 online submissions for 01 Matrix.
# Memory Usage: 17.1 MB, less than 71.63% of Python3 online submissions for 01 Matrix.
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        height = len(mat)
        width = len(mat[0])
        zeros = []
        for i in range(height):
            for j in range(width):
                if mat[i][j] == 0:
                    zeros.append((i, j)) # create a tuple with the coordinates
                else:
                    mat[i][j] = -1
        
        #  0  0  0
        #  0 -1  0
        # -1 -1 -1
        # zeros = [ (0,0), (0,1), (0, 2), (1,0), (2, 0)]
        proximity_check = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        
        for y, x in zeros:
            for y_off, x_off in proximity_check:
                dy = y + y_off
                dx = x + x_off
                if 0 <= dy < height and 0 <= dx < width and mat[dy][dx] == -1:
                    mat[dy][dx] = mat[y][x] + 1
                    zeros.append((dy, dx))
        return mat
    
# FAILED: recursion stack exceeded :(
# class Solution:
    
#     def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
#         m = len(mat)
#         n = len(mat[0])
#         def find_nearest_zero(row, col) -> int:

#             if mat[row][col] == 0:
#                 return 0
#             if row < 0 or col < 0 or row >= m or col >= n:
#                 return max(m, n)
            
#             return 1 + min(
#                 find_nearest_zero(row - 1, col),
#                 find_nearest_zero(row + 1, col),
#                 find_nearest_zero(row , col - 1),
#                 find_nearest_zero(row , col + 1)
#             ) 

#         for row in range(0, len(mat)):
#             for col in range(0, len(mat[row])):

#                 if mat[row][col] != 0:
#                     mat[row][col] = find_nearest_zero(row, col)
#         return mat
        
# @lc code=end

