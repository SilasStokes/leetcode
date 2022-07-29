#
# @lc app=leetcode id=543 lang=python3
#
# [543] Diameter of Binary Tree
#
from typing import Optional
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

# @lc code=start
# Definition for a binary tree node.
class Solution:

    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        max_diameter = 0

        def height(node):
            nonlocal max_diameter
            if not node: 
                return 0
            left = height(node.left)
            right = height(node.right)
            max_diameter = max(self.max_diameter, left + right)
            return 1 + max(left, right)

        height(root)
        return max_diameter
        
