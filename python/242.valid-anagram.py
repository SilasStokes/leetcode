#
# @lc app=leetcode id=242 lang=python3
#
# [242] Valid Anagram
#

# My naive python solution. Will be looking at the discussion.
# Accepted
# 36/36 cases passed (110 ms)
# Your runtime beats 10.5 % of python3 submissions
# Your memory usage beats 66.36 % of python3 submissions (14.4 MB)
# @lc code=start
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(s) :
            return False
        
        ascii_map = [0] * 26 
        for c in s:
            ascii_map[ord(c) - ord('a')]+=1

        for c in t:
            ascii_map[ord(c) - ord('a')]-=1

        return not any(ascii_map)
        # for c in ascii_map:
        #     if c != 0:
        #         return False
        # return True
# @lc code=end

