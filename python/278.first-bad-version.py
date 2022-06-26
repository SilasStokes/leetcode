#
# @lc app=leetcode id=278 lang=python3
#
# [278] First Bad Version
#

# @lc code=start
# The isBadVersion API is already defined for you.
# def isBadVersion(version: int) -> bool:

class Solution:
    def firstBadVersion(self, n: int) -> int:
        lbound, rbound = 0, n
        i = (lbound + rbound ) // 2

        while lbound <= rbound:
            i1, i2 = isBadVersion(i), isBadVersion(i+1)
            if i1 != i2:
                return i+1

            if i1 == True:  # i2 == True is implicit
                rbound = i - 1
            else:
                lbound = i + 1
            i = (lbound + rbound ) // 2

        return None

               
# @lc code=end

