#
# @lc app=leetcode id=876 lang=python3
#
# [876] Middle of the Linked List
#
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
from typing import Optional

# @lc code=start
# Definition for singly-linked list.


class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # rabbit = head
        hare = head

        while hare and hare.next:
            head = head.next
            hare = hare.next.next
        
        return head

        
# @lc code=end

