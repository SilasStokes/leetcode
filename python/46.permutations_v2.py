#
# @lc app=leetcode id=46 lang=python3
#
# [46] Permutations
#
# https://leetcode.com/problems/permutations/description/
#
# algorithms
# Medium (73.97%)
# Likes:    14448
# Dislikes: 244
# Total Accepted:    1.5M
# Total Submissions: 2M
# Testcase Example:  '[1,2,3]'
#
# Given an array nums of distinct integers, return all the possible
# permutations. You can return the answer in any order.
# 
# 
# Example 1:
# Input: nums = [1,2,3]
# Output: [[1,2,3],[1,3,2],[2,1,3],[2,3,1],[3,1,2],[3,2,1]]
# Example 2:
# Input: nums = [0,1]
# Output: [[0,1],[1,0]]
# Example 3:
# Input: nums = [1]
# Output: [[1]]
# 
# 
# Constraints:
# 
# 
# 1 <= nums.length <= 6
# -10 <= nums[i] <= 10
# All the integers of nums are unique.
# 
# 
#

from typing import List
# @lc code=start

class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        permutations = []
        perms = []
        def dfs(i, ints):
            choose = ints[i]
            nnums = ints[:i] + ints[i+1:]
            perms.append(choose)
            if nnums:
                for j in range(0, len(nnums)):
                    dfs(j, nnums)
                    perms.pop()
            else:
                permutations.append(perms.copy())
                return
        
        for i in range(0, len(nums)):
            dfs(i, nums)
            perms.pop()
        return permutations
        
# @lc code=end

# Use decision tree:
#                                     
#                                       1           dfs(0, [1,2,3]), choose 1 nnums = [2,3], perms = [1]
#                                                       dfs(0, [2,3]),   choose 2   nnums = [3],     perms = [1,2]
#                                                           dfs(0, [3])      choose 3   nnums = [],   perms = [1,2,3] -> permutations = [[1,2,3]]
#                                                       dfs(1, [2, 3])   choose 3   nnums = [2],     perms = [1,3]
#                                                           dfs(0, [2])      choose 2   nnums = []    perms = [1,3,2] -> permutations = [[1,2,3], [1, 3, 2]]
#                                                   
#                                                   dfs(1, [1,2,3])                                                    
#                                    2     3
#                                 3          2