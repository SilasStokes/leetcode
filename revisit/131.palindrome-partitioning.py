#
# @lc app=leetcode id=131 lang=python3
#
# [131] Palindrome Partitioning
#
# https://leetcode.com/problems/palindrome-partitioning/description/
#
# algorithms
# Medium (61.53%)
# Likes:    10109
# Dislikes: 322
# Total Accepted:    612.9K
# Total Submissions: 949.6K
# Testcase Example:  '"aab"'
#
# Given a string s, partition s such that every substring of the partition is a
# palindrome. Return all possible palindrome partitioning of s.
# 
# 
# Example 1:
# Input: s = "aab"
# Output: [["a","a","b"],["aa","b"]]
# Example 2:
# Input: s = "a"
# Output: [["a"]]
# 
# 
# Constraints:
# 
# 
# 1 <= s.length <= 16
# s contains only lowercase English letters.
# 
# 
#
from ast import List

# @lc code=start
class Solution:
    def partition(self, s: str) -> List[List[str]]:
        res = []
        part = []
        def isPalidrome(string:str, l:int, r:int):
            while l < r:
                if s[l] != s[r]:
                    return False
                l, r = l + 1, r -1
            return True    

        def dfs(i: int = 0):
            if i >= len(s):
                res.append(part.copy())
                return
            for j in range(i, len(s)):
                if isPalidrome(s, i, j):
                    part.append(s[i:j+1])
                    dfs(j+1)
                    part.pop()
        dfs(0)
        return res
     

        
# @lc code=end

