#
# @lc app=leetcode id=102 lang=python3
#
# [102] Binary Tree Level Order Traversal
#
from typing import Optional, List


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


# @lc code=start
# Definition for a binary tree node.
import queue


class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []

        debug = root.val == 1
        ans = []
        q = queue.Queue()
        q.put(root)
        cur_level_len = 1
        next_level_len = 0
        level = []
        while not q.empty():
            n = q.get()
            cur_level_len -= 1
            level.append(n.val)
            if n.left:
                q.put(n.left)
                next_level_len += 1

            if n.right:
                next_level_len += 1
                q.put(n.right)

            if cur_level_len == 0:  # we are at another level
                ans.append(level)
                cur_level_len = next_level_len
                next_level_len = 0
                level = []

        return ans


# @lc code=end
