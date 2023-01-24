#
# @lc app=leetcode id=875 lang=python3
#
# [875] Koko Eating Bananas
#
# https://leetcode.com/problems/koko-eating-bananas/description/
#
# algorithms
# Medium (53.13%)
# Likes:    5501
# Dislikes: 249
# Total Accepted:    247.2K
# Total Submissions: 473.6K
# Testcase Example:  '[3,6,7,11]\n8'
#
# Koko loves to eat bananas. There are n piles of bananas, the i^th pile has
# piles[i] bananas. The guards have gone and will come back in h hours.
# 
# Koko can decide her bananas-per-hour eating speed of k. Each hour, she
# chooses some pile of bananas and eats k bananas from that pile. If the pile
# has less than k bananas, she eats all of them instead and will not eat any
# more bananas during this hour.
# 
# Koko likes to eat slowly but still wants to finish eating all the bananas
# before the guards return.
# 
# Return the minimum integer k such that she can eat all the bananas within h
# hours.
# 
# 
# Example 1:
# 
# 
# Input: piles = [3,6,7,11], h = 8
# Output: 4
# 
# 
# Example 2:
# 
# 
# Input: piles = [30,11,23,4,20], h = 5
# Output: 30
# 
# 
# Example 3:
# 
# 
# Input: piles = [30,11,23,4,20], h = 6
# Output: 23
# 
# 
# 
# Constraints:
# 
# 
# 1 <= piles.length <= 10^4
# piles.length <= h <= 10^9
# 1 <= piles[i] <= 10^9
# 
# 
#

# @lc code=start
from typing import List

class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        if h == len(piles):
            return max(piles)

        l, r = 1, max(piles)
        
        min_k = r # max(piles)
        while l <= r:
            k = (r - l )// 2 + l
            num_hrs = 0
            for i in piles:
                num_hrs = num_hrs + -( -i// k ) # this is python ceiling division
            if num_hrs <= h:
                r = k - 1
                min_k = min(k, min_k)
            elif num_hrs > h :
                l = k + 1

            k  = (r - l )// 2 + l

        return min_k
# @lc code=end

