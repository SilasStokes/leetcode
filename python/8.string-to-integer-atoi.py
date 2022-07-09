#
# @lc app=leetcode id=8 lang=python3
#
# [8] String to Integer (atoi)
#

# @lc code=start

# this is really bad, whipped it because connor asked me to try it. True interview xonditions i guess haha
# Accepted
# 1082/1082 cases passed (57 ms)
# Your runtime beats 44.68 % of python3 submissions
# Your memory usage beats 29.82 % of python3 submissions (13.9 MB)


class Solution:
    def myAtoi(self, s: str) -> int:
        MAX = 2**31 - 1
        MIN = -2**31
        cp = 0
        s = s.strip()
        if not cp < len(s): return 0

        positive = True
        if s[cp] == '-':
            positive = False

        if s[cp] == '-' or s[cp] == '+':
            cp += 1

        if not cp < len(s): return 0
        if not ord('0') <= ord(s[cp]) <= ord('9'): return 0
        
        ans = 0
        
        multiplier = 1 if positive else -1
        temp_cp = cp + 1
        while temp_cp < len(s) and ord('0') <= ord(s[temp_cp]) <= ord('9'):
            multiplier *= 10
            temp_cp += 1

        while cp < len(s):
            if not ord('0') <= ord(s[cp]) <= ord('9'): return ans
            v = ord(s[cp]) - ord('0')
            v = v * multiplier
            ans += v
            if ans > MAX:
                return MAX
            if ans < MIN:
                return MIN
            multiplier = multiplier // 10
            cp +=1
        return ans 
        
# @lc code=end

