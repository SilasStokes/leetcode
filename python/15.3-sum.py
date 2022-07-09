#
# @lc app=leetcode id=15 lang=python3
#
# [15] 3Sum
#

# 7/9/22
# solve based on neetcode.io solution. Watched his video and then attempted to solve a few hours later. 
# helped to solve 2sumII first to get an idea for the double pointer business
# Accepted
# 311/311 cases passed (1422 ms)
# Your runtime beats 45.98 % of python3 submissions
# Your memory usage beats 42.08 % of python3 submissions (18.2 MB)

# @lc code=start
class Solution:
    # [-1,0,1,2,-1,-4] -> [-1, -1, 0, 1, 2, 4]
    def threeSum(self, nums: List[int]) -> List[List[int]]:

        nums.sort()
        ans = []

        for i, base in enumerate(nums):

            if i and nums[i - 1] == base:
                continue

            left, right = i + 1, len(nums) - 1

            while left < right:
                b, c = nums[left], nums[right]

                if b + c > -base:
                    right -= 1
                elif b + c < -base:
                    left += 1
                else:
                    ans.append([base, b , c])
                    left += 1
                    while left < right and b == nums[left]:
                        left +=1
            
        return ans

# @lc code=end

