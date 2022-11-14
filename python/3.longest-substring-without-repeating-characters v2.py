#
# @lc app=leetcode id=3 lang=python3
#
# [3] Longest Substring Without Repeating Characters
#
# https://leetcode.com/problems/longest-substring-without-repeating-characters/description/
#
# algorithms
# Medium (33.63%)
# Likes:    30158
# Dislikes: 1290
# Total Accepted:    4M
# Total Submissions: 11.9M
# Testcase Example:  '"abcabcbb"'
#
# Given a string s, find the length of the longest substring without repeating
# characters.
# 
# 
# Example 1:
# 
# 
# Input: s = "abcabcbb"
# Output: 3
# Explanation: The answer is "abc", with the length of 3.
# 
# 
# Example 2:
# 
# 
# Input: s = "bbbbb"
# Output: 1
# Explanation: The answer is "b", with the length of 1.
# 
# 
# Example 3:
# 
# 
# Input: s = "pwwkew"
# Output: 3
# Explanation: The answer is "wke", with the length of 3.
# Notice that the answer must be a substring, "pwke" is a subsequence and not a
# substring.
# 
# 
# 
# Constraints:
# 
# 
# 0 <= s.length <= 5 * 10^4
# s consists of English letters, digits, symbols and spaces.
# 
# 
#

# 

# @lc code=start
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        max_length = 0 
        l, r = 0, 0       

        seen_letters = set()
        # a b c a b c b b
        # l
        #   r
        # set = a

        # p w j w k e w
        #     l
        #       r
        # set = p j w
        while r < len(s):
            while s[r] in seen_letters:
                seen_letters.remove(s[l])
                l += 1
            # if s[r] in seen_letters:
            #     while s[l] != s[r]:
            #         seen_letters.remove(s[l])
            #         l += 1
            #     l += 1
            seen_letters.add(s[r])
            max_length = max(max_length, r - l + 1)
            r += 1

        return max_length

# @lc code=end

