#
# @lc app=leetcode id=39 lang=python3
#
# [39] Combination Sum
#
# @lc code=start

class Solution:

    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        # candidates.sort()
        length = len(candidates)
        res = []

        def dfs(val, index, buf):
            # if val < 0:
            #     return
            if val == 0:
                res.append(buf)
                return

            for i in range(index, length):
                diff = val - candidates[i]
                if diff < 0:
                    continue
                dfs(diff , i, buf + [candidates[i]])

        dfs(target, 0, [])

        return res

# [[2,7],[],[3,3,3],[],[]]
# [[],[],[],[1,1,1,1,1,2,2],[1,1,1,1,2,3],[1,1,1,1,5],[1,1,1,2,2,2],[1,1,1,3,3],[1,1,1,6],[1,1,2,2,3],[1,1,2,5],[1,1,7],[1,2,2,2,2],[1,2,3,3],[1,2,6],[1,3,5],[2,2,2,3],[2,2,5],[2,7],[3,3,3],[3,6]]
        
# @lc code=end


# https://leetcode.com/problems/combination-sum/description/
#
# algorithms
# Medium (65.68%)
# Likes:    12311
# Dislikes: 257
# Total Accepted:    1.2M
# Total Submissions: 1.8M
# Testcase Example:  '[2,3,6,7]\n7'
#
# Given an array of distinct integers candidates and a target integer target,
# return a list of all unique combinations of candidates where the chosen
# numbers sum to target. You may return the combinations in any order.
# 
# The same number may be chosen from candidates an unlimited number of times.
# Two combinations are unique if the frequency of at least one of the chosen
# numbers is different.
# 
# It is guaranteed that the number of unique combinations that sum up to target
# is less than 150 combinations for the given input.
# 
# 
# Example 1:
# 
# 
# Input: candidates = [2,3,6,7], target = 7
# Output: [[2,2,3],[7]]
# Explanation:
# 2 and 3 are candidates, and 2 + 2 + 3 = 7. Note that 2 can be used multiple
# times.
# 7 is a candidate, and 7 = 7.
# These are the only two combinations.
# 
# 
# Example 2:
# 
# 
# Input: candidates = [2,3,5], target = 8
# Output: [[2,2,2,2],[2,3,3],[3,5]]
# 
# 
# Example 3:
# 
# 
# Input: candidates = [2], target = 1
# Output: []
# 
# 
# 
# Constraints:
# 
# 
# 1 <= candidates.length <= 30
# 1 <= candidates[i] <= 200
# All elements of candidates are distinct.
# 1 <= target <= 500
# 
# 
#
