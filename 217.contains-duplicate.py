#
# @lc app=leetcode id=217 lang=python3
#
# [217] Contains Duplicate
#

# @lc code=start
class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        return len(nums) > len(set(nums))

    # def containsDuplicate(self, nums: List[int]) -> bool:

    #     dic = []
    #     for e in nums:
    #         if e not in dic:
    #             dic[e] = 1
    #         else:
    #             return True
    #     for value in dic.values():
    #         if value > 1: return True
    #     return False

            
        
# @lc code=end

