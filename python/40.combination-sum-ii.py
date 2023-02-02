#
# @lc app=leetcode id=40 lang=python3
#
# [40] Combination Sum II
#
# https://leetcode.com/problems/combination-sum-ii/description/
#
# algorithms
# Medium (53.03%)
# Likes:    7795
# Dislikes: 196
# Total Accepted:    700.1K
# Total Submissions: 1.3M
# Testcase Example:  '[10,1,2,7,6,1,5]\n8'
#
# Given a collection of candidate numbers (candidates) and a target number
# (target), find all unique combinations in candidates where the candidate
# numbers sum to target.
# 
# Each number in candidates may only be used once in the combination.
# 
# Note: The solution set must not contain duplicate combinations.
# 
# 
# Example 1:
# 
# 
# Input: candidates = [10,1,2,7,6,1,5], target = 8
# Output: 
# [
# [1,1,6],
# [1,2,5],
# [1,7],
# [2,6]
# ]
# 
# 
# Example 2:
# 
# 
# Input: candidates = [2,5,2,1,2], target = 5
# Output: 
# [
# [1,2,2],
# [5]
# ]
# 
# 
# 
# Constraints:
# 
# 
# 1 <= candidates.length <= 100
# 1 <= candidates[i] <= 50
# 1 <= target <= 30
# 
# 
#
from ast import List

# @lc code=start
class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        candidates.sort()

        def backtrack(index:int = 0, comb: List[int] = [], sum:int = 0):
            if sum==target:
                res.append(comb.copy())
                return
            if sum > target:
                return
            prev = -1
            for i in range(index, len(candidates)):
                if candidates[i] == prev:
                    continue
                comb.append(candidates[i])
                backtrack(i+1, comb, sum=candidates[i] + sum)
                comb.pop()
                prev = candidates[i]

        backtrack(comb=[], sum=0)
        return res
        
# @lc code=end