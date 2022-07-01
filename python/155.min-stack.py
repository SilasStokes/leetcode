#
# @lc app=leetcode id=155 lang=python3
#
# [155] Min Stack
#
# Accepted
# 31/31 cases passed (85 ms)
# Your runtime beats 64.79 % of python3 submissions
# Your memory usage beats 13.19 % of python3 submissions (18.5 MB)

# @lc code=start
class MinStack:

    def __init__(self):
        self.stack = []

    def push(self, val: int) -> None:
        cur_min = 0
        if not self.stack :
            cur_min = val
        else:
            cur_min = self.stack[-1][1]

        if val < cur_min:
            cur_min = val
        self.stack.append((val, cur_min))
        return None

    def pop(self) -> None:

        if self.stack:
            self.stack.pop()
        return None
        

    def top(self) -> int:
        return self.stack[-1][0] if self.stack else None
        

    def getMin(self) -> int:
        return self.stack[-1][1] if self.stack else None
        


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()
# @lc code=end

