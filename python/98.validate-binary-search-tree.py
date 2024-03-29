#
# @lc app=leetcode id=98 lang=python3
#
# [98] Validate Binary Search Tree
#
# https://leetcode.com/problems/validate-binary-search-tree/description/
#
# algorithms
# Medium (31.47%)
# Likes:    13305
# Dislikes: 1075
# Total Accepted:    1.8M
# Total Submissions: 5.6M
# Testcase Example:  '[2,1,3]'
#
# Given the root of a binary tree, determine if it is a valid binary search
# tree (BST).
# 
# A valid BST is defined as follows:
# 
# 
# The left subtree of a node contains only nodes with keys less than the node's
# key.
# The right subtree of a node contains only nodes with keys greater than the
# node's key.
# Both the left and right subtrees must also be binary search trees.
# 
# 
# 
# Example 1:
# 
# 
# Input: root = [2,1,3]
# Output: true
# 
# 
# Example 2:
# 
# 
# Input: root = [5,1,4,null,null,3,6]
# Output: false
# Explanation: The root node's value is 5 but its right child's value is 4.
# 
# 
# 
# Constraints:
# 
# 
# The number of nodes in the tree is in the range [1, 10^4].
# -2^31 <= Node.val <= 2^31 - 1
# 
# 
#

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
from math import inf
from typing import Optional
# @lc code=start
# Definition for a binary tree node.


class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        if not root: return None

        def dfs(node, minimum, maximum):
            if not node:
                return True
            return node.val > minimum and node.val < maximum and dfs(node.left, minimum, node.val) and dfs(node.right, node.val, maximum)
        
        return dfs(root, -inf, inf)
# @lc code=end

