#
# @lc app=leetcode id=143 lang=python3
#
# [143] Reorder List
#
# https://leetcode.com/problems/reorder-list/description/
#
# algorithms
# Medium (50.00%)
# Likes:    7631
# Dislikes: 265
# Total Accepted:    599.3K
# Total Submissions: 1.2M
# Testcase Example:  '[1,2,3,4]'
#
# You are given the head of a singly linked-list. The list can be represented
# as:
# 
# 
# L0 → L1 → … → Ln - 1 → Ln
# 
# 
# Reorder the list to be on the following form:
# 
# 
# L0 → Ln → L1 → Ln - 1 → L2 → Ln - 2 → …
# 
# 
# You may not modify the values in the list's nodes. Only nodes themselves may
# be changed.
# 
# 
# Example 1:
# 
# 
# Input: head = [1,2,3,4]
# Output: [1,4,2,3]
# 
# 
# Example 2:
# 
# 
# Input: head = [1,2,3,4,5]
# Output: [1,5,2,4,3]
# 
# 
# 
# Constraints:
# 
# 
# The number of nodes in the list is in the range [1, 5 * 10^4].
# 1 <= Node.val <= 1000
# 
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
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        if not head or head.next is None:
            return head
        
        slow = head
        fast = head.next
        while fast:
            slow = slow.next
            fast = fast.next
            if fast:
                fast = fast.next
        
        # reverse the latter half of the linked list
        n = slow.next
        slow.next = None
        prev = None
        while n:
            next = n.next
            n.next = prev
            prev = n
            n = next

        l1 = head
        l2 = prev 

        # print(f'l1:')
        # while l1:
        #     print(f'    {l1.val}')
        #     l1 = l1.next

        # print(f'l2:')
        # while l2:
        #     print(f'    {l2.val}')
        #     l2 = l2.next

        while l1 and l2:
            l1next = l1.next
            l2next = l2.next
            l1.next = l2
            l2.next = l1next

            l1 = l1next
            l2 = l2next

        # l1 = head
        # print(f'l1:')
        # while l1:
        #     print(f'    {l1.val}')
        #     l1 = l1.next


# @lc code=end

