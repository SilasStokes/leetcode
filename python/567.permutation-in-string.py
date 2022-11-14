#
# @lc app=leetcode id=567 lang=python3
#
# [567] Permutation in String
#
# https://leetcode.com/problems/permutation-in-string/description/
#
# algorithms
# Medium (44.05%)
# Likes:    7523
# Dislikes: 250
# Total Accepted:    508.1K
# Total Submissions: 1.2M
# Testcase Example:  '"ab"\n"eidbaooo"'
#
# Given two strings s1 and s2, return true if s2 contains a permutation of s1,
# or false otherwise.
# 
# In other words, return true if one of s1's permutations is the substring of
# s2.
# 
# 
# Example 1:
# 
# 
# Input: s1 = "ab", s2 = "eidbaooo"
# Output: true
# Explanation: s2 contains one permutation of s1 ("ba").
# 
# 
# Example 2:
# 
# 
# Input: s1 = "ab", s2 = "eidboaoo"
# Output: false
# 
# 
# 
# Constraints:
# 
# 
# 1 <= s1.length, s2.length <= 10^4
# s1 and s2 consist of lowercase English letters.
# 
# 
#

# @lc code=start
# s1 = [ a: 1, b : 1, c : 0, d : 0]
# s2 = 

class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        def index(s : str) -> int:
            return ord(s) - ord('a')
        
        if len(s1) > len(s2):
            return False

        s1_count = [0] * 26
        s2_count = [0] * 26
        for c in s1:
            s1_count[index(c)] += 1

        matches = 0
        l, r = 0, 0
        while r < len(s2) and r < len(s1):
            s2_count[index(s2[r])] += 1
            r += 1

        for i in range(len(s1_count)):
            if s1_count[i] == s2_count[i]:
                matches += 1
        while r < len(s2):
            if matches == 26: return True

            # figure out r
            i = index(s2[r])
            s2_count[i] += 1
            if s2_count[i] == s1_count[i]:
                matches += 1
            elif s2_count[i] == s1_count[i] + 1: # if it was a match and is no longer
                matches -= 1
            r += 1
            
            # figure out l
            i = index(s2[l])
            s2_count[i] -= 1
            if s2_count[i] == s1_count[i]:
                matches += 1
            elif s2_count[i] == s1_count[i] -1: # if it was a match and is no longer
                matches -= 1
            l += 1

        
        return matches == 26



        
# @lc code=end


        # while l < len(s2):
        #     r = l
        #     # s2_count = [0] * 26
        #     while r < len(s2) and r < l + len(s1):
        #         # check if the letter exists in s1_count
        #         if s1_count[index(s2[r])] == 0:
        #             break
        #         # so this is if the letter exists inside s1
        #         # we want to increase the count of `count` until it matches s1 count
        #         # s2_count[index(s2[r])] += 1
        #         # get rid of this to get rid of time limit exceeding...
        #         # if s1_count == s2_count:
        #         #     return True
        #         r += 1
        #     l += 1
        # return False