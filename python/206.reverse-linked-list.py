#
# @lc app=leetcode id=206 lang=python3
#
# [206] Reverse Linked List
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
# Accepted
# 28/28 cases passed (79 ms)
# Your runtime beats 7.57 % of python3 submissions
# Your memory usage beats 93.71 % of python3 submissions (15.4 MB)
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next:
            return head
        
        hmone = head
        head = head.next
        hpone = head.next

        hmone.next = None
        while hpone:
            head.next = hmone
            hmone = head
            head = hpone
            hpone = hpone.next
        head.next = hmone
        return head
            



# @lc code=end

