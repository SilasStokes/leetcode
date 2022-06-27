#
# @lc app=leetcode id=383 lang=python3
#
# [383] Ransom Note
#

# Accepted
# 126/126 cases passed (138 ms)
# Your runtime beats 16.13 % of python3 submissions
# Your memory usage beats 52 % of python3 submissions (14.1 MB)
# Time Complexity : O(m * n) where m and n are len(ransomNote) and len(magazine)
# Space Complexity: O(1) since we allocate a constant size array

# @lc code=start
class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        check = [0] * (1 + ord('z') - ord('a'))

        for char in magazine:
            index = ord(char) - ord('a')
            check[index] += 1

        for char in ransomNote:
            index = ord(char) - ord('a')
            check[index] -= 1
        
        for index in check:
            if index < 0:
                return False
        return True
    
    ## Another solution 
    # def canConstruct(self, ransomNote: str, magazine: str) -> bool:
    #     for i in set(ransomNote):
    #         if ransomNote.count(i) > magazine.count(i):
    #             return False
    #     return True
        
# @lc code=end

