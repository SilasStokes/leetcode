#
# @lc app=leetcode id=33 lang=python3
#
# [33] Search in Rotated Sorted Array
#
# https://leetcode.com/problems/search-in-rotated-sorted-array/description/
#
# algorithms
# Medium (38.38%)
# Likes:    18603
# Dislikes: 1106
# Total Accepted:    1.8M
# Total Submissions: 4.7M
# Testcase Example:  '[4,5,6,7,0,1,2]\n0'
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
from typing import List
# @lc code=start
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l, r = 0, len(nums) - 1
        while l <= r:
            i = (r - l) // 2 + l 
            print(f'{l=}, {r=}, {i=}')
            if nums[i] == target:
                return i

            if nums[r] < nums[l]:
                print(f'\tspanning a pivot bc {nums[r]} < {nums[l]}')
                # check if it is within the range
                if target > nums[r] and target < nums[l]:
                    return -1

                # we're spanning the pivot, decide which side of the pivot to go to? 
                if target > nums[r]: # it's in the left side
                    # check to see if we can move the right pointer over
                    newr = (i - 1 )
                    if nums[newr] < target:
                        l = newr
                    else:
                        r = newr

                elif target < nums[l]: # it's on the right side of the pivot
                    newl = (i + 1)
                    if nums[newl] > target:
                        r = newl
                    else:
                        l = newl
                else:
                    return -1
                continue
            print(f'Not spanning a pivot, binary search as normal')
            if nums[i] < target:
                l = i + 1
            else:
                r = i - 1
        return -1
# 
        
# @lc code=end

