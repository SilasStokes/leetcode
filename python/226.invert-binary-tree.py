#
# @lc app=leetcode id=226 lang=python3
#
# [226] Invert Binary Tree
#

# Runtime: 46 ms, faster than 49.74% of Python3 online submissions for Invert Binary Tree.
# Memory Usage: 13.7 MB, less than 95.84% of Python3 online submissions for Invert Binary Tree.

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


# My solution:
# class Solution:
#     def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
#         if not root:
#             return None

#         temp = root.left
#         root.left = root.right
#         root.right = temp

#         self.invertTree(root=root.left)
#         self.invertTree(root=root.right)

#         return root
        
# Solution from leet code for studying:
class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if root:
            root.left, root.right = self.invertTree(root.right), self.invertTree(root.left)
            return root

# @lc code=end


class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        stack = [root]
        while stack:
            node = stack.pop()
            if node:
                node.left, node.right = node.right, node.left
                stack.extend([node.right, node.left])
        return root
