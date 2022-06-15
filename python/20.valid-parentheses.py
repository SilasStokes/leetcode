#
# @lc app=leetcode id=20 lang=python3
#
# [20] Valid Parentheses
#

# Accepted
# 91/91 cases passed (38 ms)
# Your runtime beats 72.41 % of python3 submissions
# Your memory usage beats 68.92 % of python3 submissions (13.9 MB)

# @lc code=start
class Solution:
	def isValid(self, s: str) -> bool:
		stack = []
		for c in s:
			if (c == '[' or c == '{' or c == '('):
				stack.append(c)
				continue
			if not stack:
				return False
			top = stack.pop()
			if (c == ']' and top != '[' or c == '}'  and top != '{' or c == ')'  and top != '('):
				return False
		
		return not stack


			


# @lc code=end
