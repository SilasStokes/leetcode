#
# @lc app=leetcode id=424 lang=python3
#
# [424] Longest Repeating Character Replacement
#
# https://leetcode.com/problems/longest-repeating-character-replacement/description/
#
# algorithms
# Medium (51.24%)
# Likes:    6611
# Dislikes: 257
# Total Accepted:    361.1K
# Total Submissions: 702.1K
# Testcase Example:  '"ABAB"\n2'
#
# You are given a string s and an integer k. You can choose any character of
# the string and change it to any other uppercase English character. You can
# perform this operation at most k times.
# 
# Return the length of the longest substring containing the same letter you can
# get after performing the above operations.
# 
# 
# Example 1:
# 
# 
# Input: s = "ABAB", k = 2
# Output: 4
# Explanation: Replace the two 'A's with two 'B's or vice versa.
# 
# 
# Example 2:
# 
# 
# Input: s = "AABABBA", k = 1
# Output: 4
# Explanation: Replace the one 'A' in the middle with 'B' and form "AABBBBA".
# The substring "BBBB" has the longest repeating letters, which is 4.
# 
# 
# 
# Constraints:
# 
# 
# 1 <= s.length <= 10^5
# s consists of only uppercase English letters.
# 0 <= k <= s.length
# 
# 
#

# @lc code=start
class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        # def ind(s: str) -> int:
        #     return ord(s) - ord('A')
        letters = {}
        _len = 0
        max_count = 0
        max_len = 0

        l, r = 0, 0 # len(s) - 1
        while r < len(s):
            _len = r - l + 1

            cur_count = letters.get(s[r], 0) + 1
            letters[s[r]] = cur_count

            max_count = max(max_count, cur_count)

            if _len - max_count <= k:
                max_len = max(max_len, _len)
            else:
                letters[s[l]] -= 1
                l += 1
            r += 1
            # if _len - max_count <= k: # if there enough available changes within the given range
            #     max_len = max(max_len, _len)
            #     r += 1
            # else:
            #     while _len - max_count > k:
            #         letters[s[l]] -= 1
            #         l += 1
            #         _len = r - l + 1
            #         max_count = max(letters.values())
        return max_len
        
# @lc code=end

