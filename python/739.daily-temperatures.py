#
# @lc app=leetcode id=739 lang=python3
#
# [739] Daily Temperatures
#
# https://leetcode.com/problems/daily-temperatures/description/
#
# algorithms
# Medium (67.71%)
# Likes:    8598
# Dislikes: 202
# Total Accepted:    491.5K
# Total Submissions: 738.5K
# Testcase Example:  '[73,74,75,71,69,72,76,73]'
#
# Given an array of integers temperatures represents the daily temperatures,
# return an array answer such that answer[i] is the number of days you have to
# wait after the i^th day to get a warmer temperature. If there is no future
# day for which this is possible, keep answer[i] == 0 instead.
# 
# 
# Example 1:
# Input: temperatures = [73,74,75,71,69,72,76,73]
# Output: [1,1,4,2,1,1,0,0]
# Example 2:
# Input: temperatures = [30,40,50,60]
# Output: [1,1,1,0]
# Example 3:
# Input: temperatures = [30,60,90]
# Output: [1,1,0]
# 
# 
# Constraints:
# 
# 
# 1 <= temperatures.length <= 10^5
# 30 <= temperatures[i] <= 100
# 
# 
#

# @lc code=start
from typing import List

# edge cases:
#   1. all ascending
#   2. all descending
#   3. all equal
#   4. 


class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        answer = [0] * len(temperatures)
        stack = []
        temps = temperatures

        for i in range(len(temps)):
            while stack:
                s_val, s_val_index = stack[-1]
                if temps[i] > s_val:
                    answer[s_val_index] = i - s_val_index
                    stack.pop()
                else:
                    break
            stack.append((temps[i], i))
        return answer

        
# @lc code=end

