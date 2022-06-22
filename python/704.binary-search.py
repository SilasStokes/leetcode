#
# @lc app=leetcode id=704 lang=python3
#
# [704] Binary Search
#

# Accepted
# 47/47 cases passed (496 ms)
# Your runtime beats 6.96 % of python3 submissions
# Your memory usage beats 71.49 % of python3 submissions (15.5 MB)
# algo: Binary search   
# @lc code=start
class Solution:
    #   0 1 2 3 4 5
    # [-1,0,3,5,9,12]
    def search(self, nums: List[int], target: int) -> int:
        # sorted in ascending order
        lbound, rbound = 0, len(nums) - 1
        while lbound <= rbound:
            index = (rbound - lbound) // 2 + lbound
            if nums[index] < target:
                lbound = index + 1
            elif nums[index] > target:
                rbound = index - 1
            else:
                return index
        
        return -1
             

# @lc code=end

