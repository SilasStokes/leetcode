/*
 * @lc app=leetcode id=4 lang=typescript
 *
 * [4] Median of Two Sorted Arrays
 *
 * https://leetcode.com/problems/median-of-two-sorted-arrays/description/
 *
 * algorithms
 * Hard (34.80%)
 * Likes:    21704
 * Dislikes: 2449
 * Total Accepted:    1.8M
 * Total Submissions: 4.9M
 * Testcase Example:  '[1,3]\n[2]'
 *
 * Given two sorted arrays nums1 and nums2 of size m and n respectively, return
 * the median of the two sorted arrays.
 * 
 * The overall run time complexity should be O(log (m+n)).
 * 
 * 
 * Example 1:
 * 
 * 
 * Input: nums1 = [1,3], nums2 = [2]
 * Output: 2.00000
 * Explanation: merged array = [1,2,3] and median is 2.
 * 
 * 
 * Example 2:
 * 
 * 
 * Input: nums1 = [1,2], nums2 = [3,4]
 * Output: 2.50000
 * Explanation: merged array = [1,2,3,4] and median is (2 + 3) / 2 = 2.5.
 * 
 * 
 * 
 * Constraints:
 * 
 * 
 * nums1.length == m
 * nums2.length == n
 * 0 <= m <= 1000
 * 0 <= n <= 1000
 * 1 <= m + n <= 2000
 * -10^6 <= nums1[i], nums2[i] <= 10^6
 * 
 * 
 */

// @lc code=start
function findMedianSortedArrays(nums1: number[], nums2: number[]): number {
    // ensure n1 is the shorter
    if (nums2.length < nums1.length) return findMedianSortedArrays(nums2, nums1)

    const totalLen = nums1.length + nums2.length;
    const half = Math.floor(totalLen / 2)
    const isOdd = totalLen % 2 === 1

    let l = 0, r = nums1.length - 1
    while (true) {
        const m1 = Math.floor((r - l) / 2) + l;
        const m2 = half - m1 - 2 // two is bc need to account for two 0 indexes

        const n1l = (m1 > -1) ? nums1[m1] : -Infinity
        const n1r = (m1 + 1 < nums1.length) ? nums1[m1 + 1] : Infinity

        const n2l = (m2 > -1) ? nums2[m2] : -Infinity
        const n2r = (m2 + 1 < nums2.length) ? nums2[m1 + 1] : Infinity

        if (n1l <= n2r && n2l <= n1r) {
            if (isOdd) {
                return Math.min(n1r, n2r)
            }
            // is even
            return (Math.max(n1l, n2l) + Math.min(n1r, n2r)) / 2
        } else if (n1l > n2r) {
            r = m1 - 1;
        } else {
            l = m1 + 1
        }
    }
};
// @lc code=end

