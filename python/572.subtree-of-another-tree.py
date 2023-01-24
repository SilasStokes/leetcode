#
# @lc app=leetcode id=572 lang=python3
#
# [572] Subtree of Another Tree
#
# https://leetcode.com/problems/subtree-of-another-tree/description/
#
# algorithms
# Easy (45.75%)
# Likes:    6598
# Dislikes: 375
# Total Accepted:    596.2K
# Total Submissions: 1.3M
# Testcase Example:  '[3,4,5,1,2]\n[4,1,2]'
#
# Given the roots of two binary trees root and subRoot, return true if there is
# a subtree of root with the same structure and node values of subRoot and
# false otherwise.
# 
# A subtree of a binary tree tree is a tree that consists of a node in tree and
# all of this node's descendants. The tree tree could also be considered as a
# subtree of itself.
# 
# 
# Example 1:
# 
# 
# Input: root = [3,4,5,1,2], subRoot = [4,1,2]
# Output: true
# 
# 
# Example 2:
# 
# 
# Input: root = [3,4,5,1,2,null,null,null,null,0], subRoot = [4,1,2]
# Output: false
# 
# 
# 
# Constraints:
# 
# 
# The number of nodes in the root tree is in the range [1, 2000].
# The number of nodes in the subRoot tree is in the range [1, 1000].
# -10^4 <= root.val <= 10^4
# -10^4 <= subRoot.val <= 10^4
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
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:

        def isSameTree(r1, r2):
            if not r1 and not r2:
                return True
            if r1 and r2 and r1.val == r2.val:
                return isSameTree(r1.left, r2.left) and isSameTree(r1.right, r2.right)
            else: return False
        
        if not root and not subRoot:
            return True
        
        if not root:
            return False

        resp = False

        if root.val == subRoot.val:
            resp = isSameTree(root, subRoot)
        
        if not resp:
            resp = self.isSubtree(root.left, subRoot) or self.isSubtree(root.right, subRoot)
        
        return resp

        
# @lc code=end

