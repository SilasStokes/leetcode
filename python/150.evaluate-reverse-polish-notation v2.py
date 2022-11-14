#
# @lc app=leetcode id=150 lang=python3
#
# [150] Evaluate Reverse Polish Notation
#
# https://leetcode.com/problems/evaluate-reverse-polish-notation/description/
#
# algorithms
# Medium (43.85%)
# Likes:    4228
# Dislikes: 743
# Total Accepted:    531.5K
# Total Submissions: 1.2M
# Testcase Example:  '["2","1","+","3","*"]'
#
# Evaluate the value of an arithmetic expression in Reverse Polish Notation.
# 
# Valid operators are +, -, *, and /. Each operand may be an integer or another
# expression.
# 
# Note that division between two integers should truncate toward zero.
# 
# It is guaranteed that the given RPN expression is always valid. That means
# the expression would always evaluate to a result, and there will not be any
# division by zero operation.
# 
# 
# Example 1:
# 
# 
# Input: tokens = ["2","1","+","3","*"]
# Output: 9
# Explanation: ((2 + 1) * 3) = 9
# 
# 
# Example 2:
# 
# 
# Input: tokens = ["4","13","5","/","+"]
# Output: 6
# Explanation: (4 + (13 / 5)) = 6
# 
# 
# Example 3:
# 
# 
# Input: tokens = ["10","6","9","3","+","-11","*","/","*","17","+","5","+"]
# Output: 22
# Explanation: ((10 * (6 / ((9 + 3) * -11))) + 17) + 5
# = ((10 * (6 / (12 * -11))) + 17) + 5
# = ((10 * (6 / -132)) + 17) + 5
# = ((10 * 0) + 17) + 5
# = (0 + 17) + 5
# = 17 + 5
# = 22
# 
# 
# 
# Constraints:
# 
# 
# 1 <= tokens.length <= 10^4
# tokens[i] is either an operator: "+", "-", "*", or "/", or an integer in the
# range [-200, 200].
# 
# 
#

# @lc code=start
from typing import List

class Solution:
    def evalRPN(self, tokens: List[str]) -> int:

        s = []
        for t in tokens:
            # print(f'stack : {s}')
            if t != '+' and t != '/' and t!= '-' and t != '*':
                s.append(int(t))
            else:
                # we have an operation.
                # ans = 0
                r = s.pop()
                l = s.pop()
                match t:
                    case '*':
                        # print(f'Doing {l} * {r}')
                        ans = l * r
                    case '/':
                        # print(f'Doing {l} // {r}')
                        # ans = l // r
                        ans = int(float(l)/r)
                    case '+':
                        # print(f'Doing {l} + {r}')
                        ans = l + r
                    case '-':
                        # print(f'Doing {l} - {r}')
                        ans = l - r
                    case _:
                        ans = 0
                        ...
                print(f'Appending {ans}')
                s.append(ans)

        return s.pop() # should be the only thing left???
        
# @lc code=end

