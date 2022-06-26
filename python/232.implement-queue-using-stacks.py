#
# @lc app=leetcode id=232 lang=python3
#
# [232] Implement Queue using Stacks
#
# Accepted
# 22/22 cases passed (53 ms)
# Your runtime beats 26.68 % of python3 submissions
# Your memory usage beats 74.11 % of python3 submissions (14 MB)

# @lc code=start
class MyQueue:
    def __init__(self):
        self.s1 = []
        self.s2 = []
        

    def push(self, x: int) -> None:
        while self.s1:
            self.s2.append(self.s1.pop())

        self.s1.append(x)

        while self.s2:
            self.s1.append(self.s2.pop())

    def pop(self) -> int:
        return self.s1.pop()

    def peek(self) -> int:
        return self.s1[-1]
        

    def empty(self) -> bool:
        return not self.s1
# @lc code=end

