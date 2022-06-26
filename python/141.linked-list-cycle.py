#
# @lc app=leetcode id=141 lang=python3
#
# [141] Linked List Cycle
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None
# Accepted
# 21/21 cases passed (54 ms)
# Your runtime beats 95.61 % of python3 submissions
# Your memory usage beats 99.9 % of python3 submissions (16.2 MB)
class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        if not head:
            return False
        
        while head is not None:
            if head.next == -1:
                return True
            head.next, head = -1, head.next
            # next = head.next
            # head.next = -1
            # head = next
        return False
    



        
# @lc code=end

