#
# @lc app=leetcode id=167 lang=python3
#
# [167] Two Sum II - Input Array Is Sorted
#

# @lc code=start
class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        if not numbers:
            return 

        lp, rp = 0, len(numbers) - 1
        while lp < rp:
            lv = numbers[lp]
            rv = numbers[rp]
            if lv +rv > target:
                rp -= 1
            elif lv + rv < target:
                lp += 1
            if lv + rv == target:
                return [lp + 1, rp + 1]
            
        

        
# @lc code=end

