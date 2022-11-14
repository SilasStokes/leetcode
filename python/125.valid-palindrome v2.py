#
# @lc app=leetcode id=125 lang=python3
#
# [125] Valid Palindrome
#
# https://leetcode.com/problems/valid-palindrome/description/
#
# algorithms
# Easy (42.97%)
# Likes:    5262
# Dislikes: 6232
# Total Accepted:    1.6M
# Total Submissions: 3.8M
# Testcase Example:  '"A man, a plan, a canal: Panama"'
#
# A phrase is a palindrome if, after converting all uppercase letters into
# lowercase letters and removing all non-alphanumeric characters, it reads the
# same forward and backward. Alphanumeric characters include letters and
# numbers.
# 
# Given a string s, return true if it is a palindrome, or false otherwise.
# 
# 
# Example 1:
# 
# 
# Input: s = "A man, a plan, a canal: Panama"
# Output: true
# Explanation: "amanaplanacanalpanama" is a palindrome.
# 
# 
# Example 2:
# 
# 
# Input: s = "race a car"
# Output: false
# Explanation: "raceacar" is not a palindrome.
# 
# 
# Example 3:
# 
# 
# Input: s = " "
# Output: true
# Explanation: s is an empty string "" after removing non-alphanumeric
# characters.
# Since an empty string reads the same forward and backward, it is a
# palindrome.
# 
# 
# 
# Constraints:
# 
# 
# 1 <= s.length <= 2 * 10^5
# s consists only of printable ASCII characters.
# 
# 
#

# @lc code=start
class Solution:
    def isPalindrome(self, s: str) -> bool:
        left = 0
        right = len(s) - 1
        while right - left > 0:
            if not s[left].isalnum():
                left = left + 1
            elif not s[right].isalnum():
                right = right - 1
            elif s[left].lower() != s[right].lower():
                return False
            else:
                left = left + 1
                right = right - 1
        return True
        # s = s.lower()
        # new_s = ''
        # for c in s:
        #     if c.isalnum():
        #         new_s = new_s + c
        # length = len(new_s)
        # i = 0
        # j = length - 1
        # for i in range(length):
        #     if new_s[i] != new_s[j]:
        #         return False
        #     if j - i < 2:
        #         break
        #     j = j - 1

        # return True
        
# @lc code=end

