#
# @lc app=leetcode id=17 lang=python3
#
# [17] Letter Combinations of a Phone Number
#
# https://leetcode.com/problems/letter-combinations-of-a-phone-number/description/
#
# algorithms
# Medium (55.09%)
# Likes:    13970
# Dislikes: 808
# Total Accepted:    1.5M
# Total Submissions: 2.6M
# Testcase Example:  '"23"'
#
# Given a string containing digits from 2-9 inclusive, return all possible
# letter combinations that the number could represent. Return the answer in any
# order.
# 
# A mapping of digits to letters (just like on the telephone buttons) is given
# below. Note that 1 does not map to any letters.
# 
# 
# Example 1:
# 
# 
# Input: digits = "23"
# Output: ["ad","ae","af","bd","be","bf","cd","ce","cf"]
# 
# 
# Example 2:
# 
# 
# Input: digits = ""
# Output: []
# 
# 
# Example 3:
# 
# 
# Input: digits = "2"
# Output: ["a","b","c"]
# 
# 
# 
# Constraints:
# 
# 
# 0 <= digits.length <= 4
# digits[i] is a digit in the range ['2', '9'].
# 
# 
#
from ast import List

# @lc code=start

class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if not digits:
            return []

        n_to_l = {
            '2': ['a', 'b', 'c'],
            '3': ['d', 'e', 'f'],
            '4': ['g', 'h', 'i'],
            '5': ['j', 'k', 'l'],
            '6': ['m', 'n', 'o'],
            '7': ['p', 'q', 'r', 's'],
            '8': ['t', 'u', 'v'],
            '9': ['w', 'x', 'y', 'z']
        }
        res = []
        let = []
        def dfs(i:int):
            if i == len(digits) :
                if len(let) == len(digits):
                    res.append(''.join(let))
                return
            
            # print(f'entering dfs on {i=}, {digits[i]=}')
            for c in n_to_l.get(digits[i], []):
                let.append(c)
                for j in range(i + 1, len(digits) + 1):
                    # print(f'calling dfs on {i=}, {j=}, {let=}')
                    dfs(j)
                let.pop()

        # for i in range(len(digits)):       
        dfs(0)
        return res
        

        
# @lc code=end

