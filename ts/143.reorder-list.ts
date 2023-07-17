/*
 * @lc app=leetcode id=143 lang=typescript
 *
 * [143] Reorder List
 *
 * https://leetcode.com/problems/reorder-list/description/
 *
 * algorithms
 * Medium (50.00%)
 * Likes:    7631
 * Dislikes: 265
 * Total Accepted:    599.3K
 * Total Submissions: 1.2M
 * Testcase Example:  '[1,2,3,4]'
 *
 * You are given the head of a singly linked-list. The list can be represented
 * as:
 * 
 * 
 * L0 → L1 → … → Ln - 1 → Ln
 * 
 * 
 * Reorder the list to be on the following form:
 * 
 * 
 * L0 → Ln → L1 → Ln - 1 → L2 → Ln - 2 → …
 * 
 * 
 * You may not modify the values in the list's nodes. Only nodes themselves may
 * be changed.
 * 
 * 
 * Example 1:
 * 
 * 
 * Input: head = [1,2,3,4]
 * Output: [1,4,2,3]
 * 
 * 
 * Example 2:
 * 
 * 
 * Input: head = [1,2,3,4,5]
 * Output: [1,5,2,4,3]
 * 
 * 
 * 
 * Constraints:
 * 
 * 
 * The number of nodes in the list is in the range [1, 5 * 10^4].
 * 1 <= Node.val <= 1000
 * 
 * 
 */

class ListNode {
    val: number
    next: ListNode | null
    constructor(val?: number, next?: ListNode | null) {
        this.val = (val === undefined ? 0 : val)
        this.next = (next === undefined ? null : next)
    }
}
// @lc code=start



/**
 Do not return anything, modify head in-place instead.
 */
function reorderList(head: ListNode | null): void {
    let slow: ListNode | null| undefined = head, fast = head;

    // get the middle
    while (slow && fast && fast.next) {
        slow = slow.next;
        fast = fast.next
        fast = fast.next
    }

    // starting w the node after slow, reverse the linked list
    if (!slow || !slow.next) return

    let reverse: ListNode | null| undefined = slow.next
    slow.next = null;
    let prev: ListNode | null| undefined = null
    while (reverse) {
        let nextt = reverse.next
        reverse.next = prev
        prev = reverse;
        reverse = nextt;
    }

    let h1: ListNode | null| undefined = head
    let h2: ListNode | null| undefined = prev
    while (h2) {
        let h1next = h1!.next
        let h2next = h2.next
        h1!.next = h2;
        h2.next = h1next
        h1 = h1next
        h2 = h2next
    }

};
// @lc code=end

