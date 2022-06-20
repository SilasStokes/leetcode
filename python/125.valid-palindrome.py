#
# @lc app=leetcode id=125 lang=python3
#
# [125] Valid Palindrome
#
# Runtime: 77 ms, faster than 41.21% of Python3 online submissions for Valid Palindrome.
# Memory Usage: 15.1 MB, less than 31.29% of Python3 online submissions for Valid Palindrome.

# @lc code=start
class Solution:
	def isPalindrome(self, s: str) -> bool:
		front = 0
		back = len(s) - 1

		while back - front > 0:
			while not s[front].isalnum() and front < back:
				front += 1
			
			while not s[back].isalnum() and back > front:
				back -= 1
			
			if s[front].upper() != s[back].upper():
				return False
			front += 1
			back -= 1
		return True
		
# @lc code=end