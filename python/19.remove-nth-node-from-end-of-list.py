#
# @lc app=leetcode id=19 lang=python3
#
# [19] Remove Nth Node From End of List
#
# https://leetcode.com/problems/remove-nth-node-from-end-of-list/description/
#
# algorithms
# Medium (39.07%)
# Likes:    13934
# Dislikes: 578
# Total Accepted:    1.8M
# Total Submissions: 4.5M
# Testcase Example:  '[1,2,3,4,5]\n2'
#
# Given the head of a linked list, remove the n^th node from the end of the
# list and return its head.
# 
# 
# Example 1:
# 
# 
# Input: head = [1,2,3,4,5], n = 2
# Output: [1,2,3,5]
# 
# 
# Example 2:
# 
# 
# Input: head = [1], n = 1
# Output: []
# 
# 
# Example 3:
# 
# 
# Input: head = [1,2], n = 1
# Output: [1]
# 
# 
# 
# Constraints:
# 
# 
# The number of nodes in the list is sz.
# 1 <= sz <= 30
# 0 <= Node.val <= 100
# 1 <= n <= sz
# 
# 
# 
# Follow up: Could you do this in one pass?
# 
#

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
from typing import Optional
# @lc code=start
# Definition for singly-linked list.


class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        if not head: return head

        if not head.next and n == 1:
            return None

        left = head
        right = head
        for _ in range(n):
            right = right.next
        
        while right and right.next:
            left = left.next
            right = right.next
        
        # if we're removing the first node. 
        if right == None: # this means that we outran the linked list, thus the left node is sitting on the removal index
            head = left.next
            left.next = None
        else: left.next = left.next.next
        return head

        
# @lc code=end

