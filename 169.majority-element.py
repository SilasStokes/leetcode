#
# @lc app=leetcode id=169 lang=python3
#
# [169] Majority Element
#
# Boyer-Moore Majority Vote Algorithm

# @lc code=start
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        major = nums[0]
        count = 0
        for num in nums:
            if count == 0:
                count +=1
                major = num
            elif major == num:
                count+=1
            else:
                count -=1
        major 


# @lc code=end

