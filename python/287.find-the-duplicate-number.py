#
# @lc app=leetcode id=287 lang=python3
#
# [287] Find the Duplicate Number
#
# https://leetcode.com/problems/find-the-duplicate-number/description/
#
# algorithms
# Medium (59.04%)
# Likes:    17338
# Dislikes: 2361
# Total Accepted:    1.1M
# Total Submissions: 1.8M
# Testcase Example:  '[1,3,4,2,2]'
#
# Given an array of integers nums containing n + 1 integers where each integer
# is in the range [1, n] inclusive.
# 
# There is only one repeated number in nums, return this repeated number.
# 
# You must solve the problem without modifying the array nums and uses only
# constant extra space.
# 
# 
# Example 1:
# 
# 
# Input: nums = [1,3,4,2,2]
# Output: 2
# 
# 
# Example 2:
# 
# 
# Input: nums = [3,1,3,4,2]
# Output: 3
# 
# 
# 
# Constraints:
# 
# 
# 1 <= n <= 10^5
# nums.length == n + 1
# 1 <= nums[i] <= n
# All the integers in nums appear only once except for precisely one integer
# which appears two or more times.
# 
# 
# 
# Follow up:
# 
# 
# How can we prove that at least one duplicate number must exist in nums?
# Can you solve the problem in linear runtime complexity?
# 
# 
#

# @lc code=start
from typing import List


class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        if not nums or len(nums) < 2:
            return None

        s, f = 0, 0

        while True:
            s = nums[s]
            f = nums[f]
            f = nums[f]
            if s == f:
                break

        s2 = 0
        while True:
            s = nums[s]
            s2 = nums[s2]
            if s == s2:
                break
        
        return s 
        
        
            

        
        
# @lc code=end


# class Solution:
#     def findDuplicate(self, nums: List[int]) -> int:
        # length = len(nums)
        # count = [0] * len(nums)
        # for n in nums:
        #     if count[n] != 0: return n
        #     count[n] += 1