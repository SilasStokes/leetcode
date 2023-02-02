#
# @lc app=leetcode id=79 lang=python3
#
# [79] Word Search
#
# https://leetcode.com/problems/word-search/description/
#
# algorithms
# Medium (40.01%)
# Likes:    12634
# Dislikes: 511
# Total Accepted:    1.2M
# Total Submissions: 3M
# Testcase Example:  '[["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]]\n"ABCCED"'
#
# Given an m x n grid of characters board and a string word, return true if
# word exists in the grid.
# 
# The word can be constructed from letters of sequentially adjacent cells,
# where adjacent cells are horizontally or vertically neighboring. The same
# letter cell may not be used more than once.
# 
# 
# Example 1:
# 
# 
# Input: board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], word
# = "ABCCED"
# Output: true
# 
# 
# Example 2:
# 
# 
# Input: board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], word
# = "SEE"
# Output: true
# 
# 
# Example 3:
# 
# 
# Input: board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], word
# = "ABCB"
# Output: false
# 
# 
# 
# Constraints:
# 
# 
# m == board.length
# n = board[i].length
# 1 <= m, n <= 6
# 1 <= word.length <= 15
# board and word consists of only lowercase and uppercase English letters.
# 
# 
# 
# Follow up: Could you use search pruning to make your solution faster with a
# larger board?
# 
#
from ast import List
from collections import Counter, defaultdict

# @lc code=start
class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        visited = set()

        def dfs(row: int = 0, col:int = 0, word_index: int = 0):
            if word_index == len(word):
                return True
            if (
                not 0 <= row < len(board) 
                or not 0 <= col < len(board[row]) 
                or board[row][col] != word[word_index] 
                or (row, col) in visited
            ):
                return False

            visited.add((row, col))
            res = dfs(row + 1, col, word_index + 1) or dfs(row - 1, col, word_index + 1) or dfs(row, col + 1, word_index + 1) or dfs(row, col - 1, word_index + 1)
            visited.remove((row,col))
            return res
        # To prevent TLE,reverse the word if frequency of the first letter is more than the last letter's
        count = defaultdict(int, sum(map(Counter, board), Counter()))
        if count[word[0]] > count[word[-1]]:
            word = word[::-1]

        for r in range(0, len(board) ):
            for c in range(0, len(board[r])):
                if dfs(r ,c ,0 ):
                    return True
        return False
        
# @lc code=end
# class Solution:
#     def exist(self, board: List[List[str]], word: str) -> bool:
#         ROWS, COLS = len(board), len(board[0])
#         path = set()

#         def dfs(r, c, i):
#             if i == len(word):
#                 return True
#             if (
#                 min(r, c) < 0
#                 or r >= ROWS
#                 or c >= COLS
#                 or word[i] != board[r][c]
#                 or (r, c) in path
#             ):
#                 return False
#             path.add((r, c))
#             res = (
#                 dfs(r + 1, c, i + 1)
#                 or dfs(r - 1, c, i + 1)
#                 or dfs(r, c + 1, i + 1)
#                 or dfs(r, c - 1, i + 1)
#             )
#             path.remove((r, c))
#             return res

#         # To prevent TLE,reverse the word if frequency of the first letter is more than the last letter's
#         count = defaultdict(int, sum(map(Counter, board), Counter()))
#         if count[word[0]] > count[word[-1]]:
#             word = word[::-1]
            
#         for r in range(ROWS):
#             for c in range(COLS):
#                 if dfs(r, c, 0):
#                     return True
#         return False

