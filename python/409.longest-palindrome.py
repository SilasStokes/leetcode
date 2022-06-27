#
# @lc app=leetcode id=409 lang=python3
#
# [409] Longest Palindrome
#
# Accepted
# 95/95 cases passed (47 ms)
# Your runtime beats 56.36 % of python3 submissions
# Your memory usage beats 20.92 % of python3 submissions (13.9 MB)

# @lc code=start
class Solution:
    def longestPalindrome(self, s: str) -> int:
        max_odd = 0
        total_sum = 0
        for c in set(s):
            count = s.count(c)
            if count % 2 == 1 and count > max_odd:
                if (max_odd != 0):
                    total_sum += (max_odd - 1)
                max_odd = count
            elif count % 2 == 1:
                total_sum += (count - 1)
            else:
                total_sum += count
        return total_sum + max_odd
        
# @lc code=end

