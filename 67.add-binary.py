#
# @lc app=leetcode id=67 lang=python3
#
# [67] Add Binary
#

# @lc code=start
## incredibly busy answer.
# Accepted
# 294/294 cases passed (56 ms)
# Your runtime beats 39.36 % of python3 submissions
# Your memory usage beats 72.49 % of python3 submissions (13.9 MB)
import math
class Solution:
    def addBinary(self, a: str, b: str) -> str:
        a_int = 0
        i = 0
        for char in reversed(a):
            temp = int(char)
            if temp == 1:
                a_int += 2**i
            i+=1

        b_int = 0
        i = 0
        for char in reversed(b):
            temp = int(char)
            if temp == 1:
                b_int += 2**i
            i += 1

        sum_int = a_int + b_int
        if sum_int == 1 :
            return '1'
        if sum_int == 0:
            return '0'

        sum_str = ""
        max_pwr = math.floor(math.log2(sum_int))

        for i in range(max_pwr, -1, -1):
            pwr = 2**i
            if pwr > sum_int:
                sum_str = sum_str + "0"
            else:
                sum_str = sum_str + '1'
                sum_int = sum_int - pwr
        return sum_str
        
# @lc code=end

