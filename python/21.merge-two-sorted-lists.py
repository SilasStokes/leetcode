#
# @lc app=leetcode id=21 lang=python
#
# [21] Merge Two Sorted Lists
#

# I am learning python so this is a solution I worked through from the LEETCODE
# discussion forum.

# @lc code=start
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next


class Solution(object):
	def mergeTwoLists(self, list1, list2 ):
		"""
		:type list1: Optional[ListNode]
		:type list2: Optional[ListNode]
		:rtype: Optional[ListNode]
		"""
		if not list1 and not list2:
			return list1
		
		if not list1 or not list2:
			return list1 if not list2 else list2
		
		seek, target = (list1, list2) if list1.val < list2.val else (list2, list1)

		head = seek

		while seek and target:
			while seek.next and seek.next.val < target.val:
				seek = seek.next
			
			(seek.next, target) = (target, seek.next)
			seek = seek.next
		return head



# @lc code=end
