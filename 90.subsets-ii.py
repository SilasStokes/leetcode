#
# @lc app=leetcode id=90 lang=python3
#
# [90] Subsets II
#
# https://leetcode.com/problems/subsets-ii/description/
#
# algorithms
# Medium (54.69%)
# Likes:    7426
# Dislikes: 210
# Total Accepted:    654.7K
# Total Submissions: 1.2M
# Testcase Example:  '[1,2,2]'
#
# Given an integer array nums that may contain duplicates, return all possible
# subsets (the power set).
# 
# The solution set must not contain duplicate subsets. Return the solution in
# any order.
# 
# 
# Example 1:
# Input: nums = [1,2,2]
# Output: [[],[1],[1,2],[1,2,2],[2],[2,2]]
# Example 2:
# Input: nums = [0]
# Output: [[],[0]]
# 
# 
# Constraints:
# 
# 
# 1 <= nums.length <= 10
# -10 <= nums[i] <= 10
# 
# 
#

# @lc code=start
class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        
# @lc code=end

