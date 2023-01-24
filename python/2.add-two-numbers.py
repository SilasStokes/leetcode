#
# @lc app=leetcode id=2 lang=python3
#
# [2] Add Two Numbers
#
# https://leetcode.com/problems/add-two-numbers/description/
#
# algorithms
# Medium (39.34%)
# Likes:    22994
# Dislikes: 4440
# Total Accepted:    3.3M
# Total Submissions: 8.2M
# Testcase Example:  '[2,4,3]\n[5,6,4]'
#
# You are given two non-empty linked lists representing two non-negative
# integers. The digits are stored in reverse order, and each of their nodes
# contains a single digit. Add the two numbers and return the sum as a linked
# list.
# 
# You may assume the two numbers do not contain any leading zero, except the
# number 0 itself.
# 
# 
# Example 1:
# 
# 
# Input: l1 = [2,4,3], l2 = [5,6,4]
# Output: [7,0,8]
# Explanation: 342 + 465 = 807.
# 
# 
# Example 2:
# 
# 
# Input: l1 = [0], l2 = [0]
# Output: [0]
# 
# 
# Example 3:
# 
# 
# Input: l1 = [9,9,9,9,9,9,9], l2 = [9,9,9,9]
# Output: [8,9,9,9,0,0,0,1]
# 
# 
# 
# Constraints:
# 
# 
# The number of nodes in each linked list is in the range [1, 100].
# 0 <= Node.val <= 9
# It is guaranteed that the list represents a number that does not have leading
# zeros.
# 
# 
#
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
from typing import Optional


class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        # def add_recursive(temp):
        #     if not temp.next:
        #         return 
        if not l1:
            return l2
        if not l2:
            return l1
        

        head = None
        prev = None
        carry = 0
        while l1 and l2:
            sum = l1.val + l2.val + carry
            carry = 0

            if sum > 9:
                carry = sum // 10
                sum = sum %10
                # print(f'inside if sum > 9, {sum=} {carry=}')

            cur = ListNode(sum)

            if not head:
                head = cur
            if prev:
                prev.next = cur
            
            prev = cur
            l1 = l1.next
            l2 = l2.next

        l3 = l1 if l1 else l2
        while l3:
            sum = l3.val + carry
            carry = 0
            if sum > 9:
                carry = sum // 10
                sum = sum %10
            cur = ListNode(sum)
            prev.next = cur
            prev = cur
            l3 = l3.next
        if carry != 0:
            cur = ListNode(carry)
            prev.next = cur

        return head

        
# @lc code=end

