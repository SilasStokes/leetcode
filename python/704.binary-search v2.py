#
# @lc app=leetcode id=704 lang=python3
#
# [704] Binary Search
#
# https://leetcode.com/problems/binary-search/description/
#
# algorithms
# Easy (55.20%)
# Likes:    7224
# Dislikes: 157
# Total Accepted:    1.4M
# Total Submissions: 2.5M
# Testcase Example:  '[-1,0,3,5,9,12]\n9'
#
# Given an array of integers nums which is sorted in ascending order, and an
# integer target, write a function to search target in nums. If target exists,
# then return its index. Otherwise, return -1.
# 
# You must write an algorithm with O(log n) runtime complexity.
# 
# 
# Example 1:
# 
# 
# Input: nums = [-1,0,3,5,9,12], target = 9
# Output: 4
# Explanation: 9 exists in nums and its index is 4
# 
# 
# Example 2:
# 
# 
# Input: nums = [-1,0,3,5,9,12], target = 2
# Output: -1
# Explanation: 2 does not exist in nums so return -1
# 
# 
# 
# Constraints:
# 
# 
# 1 <= nums.length <= 10^4
# -10^4 < nums[i], target < 10^4
# All the integers in nums are unique.
# nums is sorted in ascending order.
# 
# 
#

# @lc code=start
from typing import List


class Solution:
    def search(self, nums: List[int], target: int) -> int:

        if target < nums[0] or target > nums[-1]:
            return -1

        l, r = 0, len(nums) - 1

        while l <= r:
            i = ( r - l ) // 2 + l
            if nums[i] == target:
                return i
            if nums[i] < target:
                l = i + 1
            else:
                r = i - 1
                


        
        return -1

        
# @lc code=end

