#
# @lc app=leetcode id=33 lang=python3
#
# [33] Search in Rotated Sorted Array
#
# https://leetcode.com/problems/search-in-rotated-sorted-array/description/
#
# algorithms
# Medium (37.85%)
# Likes:    16115
# Dislikes: 986
# Total Accepted:    1.6M
# Total Submissions: 4.2M
# Testcase Example:  '[4,5,6,7,0,1,2]\n0'
# @lc code=start
from math import inf


class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l, h = 0, len(nums) 

        while l < h:

            # get middle
            m = (l + h) // 2 # 1 // 2 = 0

            n = 0
            # check if we're dealing w the right side where
            # the middle is on the right side of pivot AND target is on the right side of the pivot
            if (nums[m] < nums[0]) == (target < nums[0]):
                n = nums[m]

            # check if we're dealing with the left side where
            # the middle is on the left side of pivot and target is on the left side of pivot
            # elif (nums[m] > nums[0]) and (target >= nums[0]):     
            #     n = nums[m]

            # if it's on the right side
            # note this ignores the middle
            elif target < nums[0]:
                n = -inf
            else:
                n = +inf
            # n = nums[m] if (nums[m] < nums[0]) == (target < nums[0]) else -inf if target < nums[0] else inf
            
            if n < target:
                l = m + 1
            elif n > target:
                h = m
            else:
                return m
        
        return -1
        
# @lc code=end


#
# There is an integer array nums sorted in ascending order (with distinct
# values).
# 
# Prior to being passed to your function, nums is possibly rotated at an
# unknown pivot index k (1 <= k < nums.length) such that the resulting array is
# [nums[k], nums[k+1], ..., nums[n-1], nums[0], nums[1], ..., nums[k-1]]
# (0-indexed). For example, [0,1,2,4,5,6,7] might be rotated at pivot index 3
# and become [4,5,6,7,0,1,2].
# 
# Given the array nums after the possible rotation and an integer target,
# return the index of target if it is in nums, or -1 if it is not in nums.
# 
# You must write an algorithm with O(log n) runtime complexity.
# 
# 
# Example 1:
# Input: nums = [4,5,6,7,0,1,2], target = 0
# Output: 4
# Example 2:
# Input: nums = [4,5,6,7,0,1,2], target = 3
# Output: -1
# Example 3:
# Input: nums = [1], target = 0
# Output: -1
# 
# 
# Constraints:
# 
# 
# 1 <= nums.length <= 5000
# -10^4 <= nums[i] <= 10^4
# All values of nums are unique.
# nums is an ascending array that is possibly rotated.
# -10^4 <= target <= 10^4
# 
# 
#
