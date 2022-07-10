# @lc code=start
class Solution:
# ["10","6","9","3","+","-11","*","/","*","17","+","5","+"]
# Stack = [10 6 9 3 ] see the plus so pop twice, 9 + 3 = 12, push that onto the stack
# stack = [10 6 12 ]
# stack = [10 6 12 -11] see the * so pop twice 12 * -11 = -132
# stack = [10 6 -132]  see the / so pop twice do 6 // 132 -> 0
# stack = [10 0] see the * so do 10 * 0
# stack = [0 17] 
# stack = [17 5] + so 22

    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        for tok in tokens:
            # print('stack = ' + format(stack) + ' examining : ' + tok)
            match tok:
                case '*':
                    n1 = stack.pop()
                    n2 = stack.pop()
                    ans = n2 * n1
                    stack.append(ans)
                case '/':
                    n1 = stack.pop()
                    n2 = stack.pop()
                    ans = int(float(n2)/n1)
                    stack.append(ans)
                case '+':
                    n1 = stack.pop()
                    n2 = stack.pop()
                    ans = n2 + n1
                    stack.append(ans)
                case '-':
                    n1 = stack.pop()
                    n2 = stack.pop()
                    ans = n2 - n1
                    stack.append(ans)
                case _:
                    stack.append(int(tok))

        return stack.pop()



        
# @lc code=end

#
# @lc app=leetcode id=150 lang=python3
#
# [150] Evaluate Reverse Polish Notation
#
# https://leetcode.com/problems/evaluate-reverse-polish-notation/description/
#
# algorithms
# Medium (42.70%)
# Likes:    3455
# Dislikes: 657
# Total Accepted:    453.5K
# Total Submissions: 1M
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
