#
# @lc app=leetcode id=230 lang=python3
#
# [230] Kth Smallest Element in a BST
#
# https://leetcode.com/problems/kth-smallest-element-in-a-bst/description/
#
# algorithms
# Medium (68.79%)
# Likes:    8891
# Dislikes: 158
# Total Accepted:    992.1K
# Total Submissions: 1.4M
# Testcase Example:  '[3,1,4,null,2]\n1'
#
# Given the root of a binary search tree, and an integer k, return the k^th
# smallest value (1-indexed) of all the values of the nodes in the tree.
# 
# 
# Example 1:
# 
# 
# Input: root = [3,1,4,null,2], k = 1
# Output: 1
# 
# 
# Example 2:
# 
# 
# Input: root = [5,3,6,2,4,null,null,1], k = 3
# Output: 3
# 
# 
# 
# Constraints:
# 
# 
# The number of nodes in the tree is n.
# 1 <= k <= n <= 10^4
# 0 <= Node.val <= 10^4
# 
# 
# 
# Follow up: If the BST is modified often (i.e., we can do insert and delete
# operations) and you need to find the kth smallest frequently, how would you
# optimize?
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
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        stack = []
        curr = root
        while stack or curr:
            while curr:
                stack.append(curr)
                curr = curr.left
            curr = stack.pop()
            k -= 1
            if k == 0:
                return curr.val
            curr = curr.right
            
        # this solution is before I realized that the binary tree was sorted lol
        # sorted_values = []  # don't have to do k + 1 bc k is 1 indexed
        # def dfs(node):
        #     nonlocal sorted_values
        #     if not node:
        #         return 
        #     if len(sorted_values) < k: # [1]
        #         sorted_values.append(node.val)
        #     elif node.val < max(sorted_values):
        #         sorted_values.sort(key= lambda x : x)
        #         sorted_values.pop()
        #         sorted_values.append(node.val)
        #     dfs(node.left)
        #     dfs(node.right)
        # dfs(root)
        # sorted_values.sort(key= lambda x : x)
        # return sorted_values[-1]

        
# @lc code=end

