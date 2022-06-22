#
# @lc app=leetcode id=53 lang=python3
#
# [53] Maximum Subarray
#

# @lc code=start


# Accepted
# 209/209 cases passed (1088 ms)
# Your runtime beats 40.71 % of python3 submissions
# Your memory usage beats 9.68 % of python3 submissions (28.5 MB)
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        max_sum = nums[0]
        sum = 0

        for n in nums:
            sum += n
            if n > sum:
                sum = n
            
            if sum > max_sum:
                max_sum = sum

        return max_sum
        
# @lc code=end

