#
# @lc app=leetcode id=130 lang=python3
#
# [130] Surrounded Regions
#
# https://leetcode.com/problems/surrounded-regions/description/
#
# algorithms
# Medium (36.49%)
# Likes:    6566
# Dislikes: 1439
# Total Accepted:    508.4K
# Total Submissions: 1.4M
# Testcase Example:  '[["X","X","X","X"],["X","O","O","X"],["X","X","O","X"],["X","O","X","X"]]'
#
# Given an m x n matrix board containing 'X' and 'O', capture all regions that
# are 4-directionally surrounded by 'X'.
# 
# A region is captured by flipping all 'O's into 'X's in that surrounded
# 
# 
# Example 1:
# 
# 
# Input: board =
# [["X","X","X","X"],["X","O","O","X"],["X","X","O","X"],["X","O","X","X"]]
# Output:
# [["X","X","X","X"],["X","X","X","X"],["X","X","X","X"],["X","O","X","X"]]
# Explanation: Notice that an 'O' should not be flipped if:
# - It is on the border, or
# - It is adjacent to an 'O' that should not be flipped.
# The bottom 'O' is on the border, so it is not flipped.
# The other three 'O' form a surrounded region, so they are flipped.
# 
# 
# Example 2:
# 
# 
# Input: board = [["X"]]
# Output: [["X"]]
# 
# 
# 
# Constraints:
# 
# 
# m == board.length
# n == board[i].length
# 1 <= m, n <= 200
# board[i][j] is 'X' or 'O'.
# 
# 
#

from ast import List
# @lc code=start
class Solution:
    """
    Do not return anything, modify board in-place instead.
    """
    def solve(self, board: List[List[str]]) -> None:
        visited = []
        def check(r:int, c:int):
            nonlocal visited
            # if they are adjacent to a the edge they cannot be surrounded.
            if not 0 <= r < len(board) or not 0 <= c < len(board[r]):
                return False
            
            if board[r][c] == 'X' or (r,c) in visited:
                return True

            visited.append((r, c))
            # this last case is if board[r][c]=='O'
            return (
                check(r + 1, c) and \
                check(r - 1, c) and \
                check(r, c + 1) and \
                check(r, c - 1)
            )
        
        for r in range(len(board)):
            for c in range( len(board[r]) ):
                res = check(r, c)
                if res and visited:
                    for rr, cc in visited:
                        board[rr][cc] = 'X'
                visited = []
        
# @lc code=end
