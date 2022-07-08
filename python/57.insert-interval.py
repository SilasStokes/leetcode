#
# @lc app=leetcode id=57 lang=python3
#
# [57] Insert Interval
#

# @lc code=start
from typing import List


class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        left_index, right_index = 0,0
        if not intervals:
            return [newInterval]

        left = []
        right =  []
        for interval in intervals:
            if interval[1] < newInterval[0]:
                left.append(interval)
            if interval[0] > newInterval[1]:
                right.append(interval)
        if left + right != intervals:
            left_index, right_index = len(left), -len( right ) - 1 #if len(right) > 0 else 0
            newInterval[0] = min(intervals[left_index][0], newInterval[0])
            newInterval[1] = max(intervals[right_index][1], newInterval[1])
        return left + [newInterval] + right

# @lc code=end

