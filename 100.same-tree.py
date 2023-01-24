#
# @lc app=leetcode id=100 lang=python3
#
# [100] Same Tree
#
# https://leetcode.com/problems/same-tree/description/
#
# algorithms
# Easy (56.09%)
# Likes:    7709
# Dislikes: 162
# Total Accepted:    1.3M
# Total Submissions: 2.3M
# Testcase Example:  '[1,2,3]\n[1,2,3]'
#
# Given the roots of two binary trees p and q, write a function to check if
# they are the same or not.
# 
# Two binary trees are considered the same if they are structurally identical,
# and the nodes have the same value.
# 
# 
# Example 1:
# 
# 
# Input: p = [1,2,3], q = [1,2,3]
# Output: true
# 
# 
# Example 2:
# 
# 
# Input: p = [1,2], q = [1,null,2]
# Output: false
# 
# 
# Example 3:
# 
# 
# Input: p = [1,2,1], q = [1,1,2]
# Output: false
# 
# 
# 
# Constraints:
# 
# 
# The number of nodes in both trees is in the range [0, 100].
# -10^4 <= Node.val <= 10^4
# 
# 
#
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

from typing import Optional

# @lc code=start
# Definition for a binary tree node.
class Solution:
    # def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
    #     if not p and not q:
    #         return True
        
    #     if p and not q or q and not p:
    #         return False

    #     if p.val == q.val:
    #         return False
        
    #     if not self.isSameTree(p.left, q.left):
    #         return False

    #     if not self.isSameTree(p.right, q.right):
    #         return False
        
    #     return True

    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        if not p and not q:
            return True

        if p and q and p.val == q.val:
            return self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)
        else:
            return False
        

        
# @lc code=end

