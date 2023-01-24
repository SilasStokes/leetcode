#
# @lc app=leetcode id=102 lang=python3
#
# [102] Binary Tree Level Order Traversal
#
# https://leetcode.com/problems/binary-tree-level-order-traversal/description/
#
# algorithms
# Medium (62.72%)
# Likes:    11711
# Dislikes: 226
# Total Accepted:    1.6M
# Total Submissions: 2.5M
# Testcase Example:  '[3,9,20,null,null,15,7]'
#
# Given the root of a binary tree, return the level order traversal of its
# nodes' values. (i.e., from left to right, level by level).
# 
# 
# Example 1:
# 
# 
# Input: root = [3,9,20,null,null,15,7]
# Output: [[3],[9,20],[15,7]]
# 
# 
# Example 2:
# 
# 
# Input: root = [1]
# Output: [[1]]
# 
# 
# Example 3:
# 
# 
# Input: root = []
# Output: []
# 
# 
# 
# Constraints:
# 
# 
# The number of nodes in the tree is in the range [0, 2000].
# -1000 <= Node.val <= 1000
# 
# 
#
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
import collections
from typing import Optional, List


class Solution:
    # def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
    #     if not root:
    #         return None
    #     levels = []
    #     queue = []
    #     lvl = []

    #     queue.insert(0, root)
    #     count = 1
    #     count2 = 0
    #     while queue:
    #         cur = queue.pop()
    #         count -= 1

    #         if cur.left:
    #             queue.insert(0, cur.left)
    #             count2 += 1

    #         if cur.right:
    #             queue.insert(0, cur.right)
    #             count2 += 1

    #         lvl.append(cur.val)
    #         if count == 0:
    #             levels.append(lvl)
    #             lvl = []
    #             count = count2
    #             count2 = 0
    #     return levels
                
    def levelOrder(self, root: TreeNode) -> List[List[int]]:
        res = []
        q = collections.deque()
        if root:
            q.append(root)

        while q:
            val = []

            for i in range(len(q)):
                node = q.popleft()
                val.append(node.val)
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
            res.append(val)
        return res
        
        
# @lc code=end

