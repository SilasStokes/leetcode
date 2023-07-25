/*
 * @lc app=leetcode id=21 lang=typescript
 *
 * [21] Merge Two Sorted Lists
 *
 * https://leetcode.com/problems/merge-two-sorted-lists/description/
 *
 * algorithms
 * Easy (61.36%)
 * Likes:    16013
 * Dislikes: 1403
 * Total Accepted:    2.8M
 * Total Submissions: 4.5M
 * Testcase Example:  '[1,2,4]\n[1,3,4]'
 *
 * You are given the heads of two sorted linked lists list1 and list2.
 * 
 * Merge the two lists in a one sorted list. The list should be made by
 * splicing together the nodes of the first two lists.
 * 
 * Return the head of the merged linked list.
 * 
 * 
 * Example 1:
 * 
 * 
 * Input: list1 = [1,2,4], list2 = [1,3,4]
 * Output: [1,1,2,3,4,4]
 * 
 * 
 * Example 2:
 * 
 * 
 * Input: list1 = [], list2 = []
 * Output: []
 * 
 * 
 * Example 3:
 * 
 * 
 * Input: list1 = [], list2 = [0]
 * Output: [0]
 * 
 * 
 * 
 * Constraints:
 * 
 * 
 * The number of nodes in both lists is in the range [0, 50].
 * -100 <= Node.val <= 100
 * Both list1 and list2 are sorted in non-decreasing order.
 * 
 * 
 */

// @lc code=start
/**
 * Definition for singly-linked list.
 * class ListNode {
 *     val: number
 *     next: ListNode | null
 *     constructor(val?: number, next?: ListNode | null) {
 *         this.val = (val===undefined ? 0 : val)
 *         this.next = (next===undefined ? null : next)
 *     }
 * }
 */

function mergeTwoLists(list1: ListNode | null, list2: ListNode | null): ListNode | null {
    if (!list1 || !list2) return list1 || list2

    if (list1.val > list2.val) return mergeTwoLists(list2, list1);

    // we know that l1 is going to have to have smaller val now
    let t1 = list1;
    let t2 = list2

    while (t1) {
        if (!t2) return list1
        if (t1.val <= t2.val ) {
            if (!t1.next) {
                t1.next = t2
                return list1
            } else if (t1.next?.val > t2.val) {
                // do an insert
                let t1next = t1.next;
                let t2next = t2.next;

                t1.next = t2;
                t2.next = t1next;
                t2 = t2next
            }
        }
        t1 = t1.next
    }
    return list1
};
// @lc code=end

