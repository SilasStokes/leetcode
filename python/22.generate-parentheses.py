#
# @lc app=leetcode id=22 lang=python3
#
# [22] Generate Parentheses
#
# https://leetcode.com/problems/generate-parentheses/description/
#
# algorithms
# Medium (71.28%)
# Likes:    15916
# Dislikes: 612
# Total Accepted:    1.3M
# Total Submissions: 1.7M
# Testcase Example:  '3'
#
# Given n pairs of parentheses, write a function to generate all combinations
# of well-formed parentheses.
# 
# 
# Example 1:
# Input: n = 3
# Output: ["((()))","(()())","(())()","()(())","()()()"]
# Example 2:
# Input: n = 1
# Output: ["()"]
# 
# 
# Constraints:
# 
# 
# 1 <= n <= 8
# 
# 
#

# @lc code=start
from typing import List

# 3
# ((()))
# (()())
# (())()
# ()(())
# ()()()

# 2 :
# (())
# ()()

# 1:
# ()


class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        parens = []
        stack = []
        def generate(open = 0, close = 0):
            if open == close == n:
                parens.append(''.join(stack))
            if open < n :
                stack.append('(')
                generate(open + 1, close)
                stack.pop()
            if close < open:
                stack.append(')')
                generate(open, close +1 )
                stack.pop()
            return

        generate()
        return parens






        
# @lc code=end

