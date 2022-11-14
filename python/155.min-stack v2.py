#
# @lc app=leetcode id=155 lang=python3
#
# [155] Min Stack
#
# https://leetcode.com/problems/min-stack/description/
#
# algorithms
# Medium (51.26%)
# Likes:    10135
# Dislikes: 687
# Total Accepted:    1.1M
# Total Submissions: 2.2M
# Testcase Example:  '["MinStack","push","push","push","getMin","pop","top","getMin"]\n' +
# '[[],[-2],[0],[-3],[],[],[],[]]'
#
# Design a stack that supports push, pop, top, and retrieving the minimum
# element in constant time.
# 
# Implement the MinStack class:
# 
# 
# MinStack() initializes the stack object.
# void push(int val) pushes the element val onto the stack.
# void pop() removes the element on the top of the stack.
# int top() gets the top element of the stack.
# int getMin() retrieves the minimum element in the stack.
# 
# 
# You must implement a solution with O(1) time complexity for each function.
# 
# 
# Example 1:
# 
# 
# Input
# ["MinStack","push","push","push","getMin","pop","top","getMin"]
# [[],[-2],[0],[-3],[],[],[],[]]
# 
# Output
# [null,null,null,null,-3,null,0,-2]
# 
# Explanation
# MinStack minStack = new MinStack();
# minStack.push(-2);
# minStack.push(0);
# minStack.push(-3);
# minStack.getMin(); // return -3
# minStack.pop();
# minStack.top();    // return 0
# minStack.getMin(); // return -2
# 
# 
# 
# Constraints:
# 
# 
# -2^31 <= val <= 2^31 - 1
# Methods pop, top and getMin operations will always be called on non-empty
# stacks.
# At most 3 * 10^4 calls will be made to push, pop, top, and getMin.
# 
# 
#

# @lc code=start
class MinStack:
    stack = []
    def __init__(self):
      self.stack = []

    def push(self, val: int) -> None:
      if not self.stack:
        self.stack.append((val, val))
      else:
        last_val, cur_min = self.stack[-1]
        if val < cur_min:
          self.stack.append((val,val))
        else:
          self.stack.append((val, cur_min))

    def pop(self) -> None:
      self.stack.pop()
      return None
        

    def top(self) -> int:
      val, cur_min  = self.stack[-1]

      return val

    def getMin(self) -> int:
      val, cur_min = self.stack[-1]
      return cur_min

# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()
# @lc code=end

