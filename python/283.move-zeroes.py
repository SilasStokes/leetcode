#
# @lc app=leetcode id=283 lang=python3
#
# [283] Move Zeroes
#

# @lc code=start
class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        zeros = 0
        for i in range(len(nums)):
            if nums[i] == 0:
                zeros += 1

            elif nums[i] != 0 and zeros > 0:
                nums[i - zeros], nums[i] = nums[i], 0 
                i += 1
        

                    


        
# @lc code=end

