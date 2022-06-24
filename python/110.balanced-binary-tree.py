#
# @lc app=leetcode id=110 lang=python3
#
# [110] Balanced Binary Tree
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
# Accepted
# 228/228 cases passed (121 ms)
# Your runtime beats 8.62 % of python3 submissions
# Your memory usage beats 61.43 % of python3 submissions (18.6 MB)
class Solution:
    def findHeight(self, root):
        if not root:
            return 0
        left = self.findHeight(root.left)
        right = self.findHeight(root.right)

        if left == -1 or right == -1 or abs(left - right) > 1 :
            return -1
        
        return max(left, right) +1



    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        height = self.findHeight(root)
        return height != -1

# @lc code=end

