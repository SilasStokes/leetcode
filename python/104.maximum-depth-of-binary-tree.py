#
# @lc app=leetcode id=104 lang=python3
#
# [104] Maximum Depth of Binary Tree
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
    def maxDepth(self, root: Optional[TreeNode]) -> int:

        def depth(root):
            if root is None:
                return 0
            left, right = depth(root.left), depth(root.right)

            return max(left, right) + 1
        
        return depth(root)


        
# @lc code=end

