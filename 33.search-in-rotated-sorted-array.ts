/*
 * @lc app=leetcode id=33 lang=typescript
 *
 * [33] Search in Rotated Sorted Array
 *
 * https://leetcode.com/problems/search-in-rotated-sorted-array/description/
 *
 * algorithms
 * Medium (38.38%)
 * Likes:    18603
 * Dislikes: 1106
 * Total Accepted:    1.8M
 * Total Submissions: 4.7M
 * Testcase Example:  '[4,5,6,7,0,1,2]\n0'
 *
 * There is an integer array nums sorted in ascending order (with distinct
 * values).
 * 
 * Prior to being passed to your function, nums is possibly rotated at an
 * unknown pivot index k (1 <= k < nums.length) such that the resulting array
 * is [nums[k], nums[k+1], ..., nums[n-1], nums[0], nums[1], ..., nums[k-1]]
 * (0-indexed). For example, [0,1,2,4,5,6,7] might be rotated at pivot index 3
 * and become [4,5,6,7,0,1,2].
 * 
 * Given the array nums after the possible rotation and an integer target,
 * return the index of target if it is in nums, or -1 if it is not in nums.
 * 
 * You must write an algorithm with O(log n) runtime complexity.
 * 
 * 
 * Example 1:
 * Input: nums = [4,5,6,7,0,1,2], target = 0
 * Output: 4
 * Example 2:
 * Input: nums = [4,5,6,7,0,1,2], target = 3
 * Output: -1
 * Example 3:
 * Input: nums = [1], target = 0
 * Output: -1
 * 
 * 
 * Constraints:
 * 
 * 
 * 1 <= nums.length <= 5000
 * -10^4 <= nums[i] <= 10^4
 * All values of nums are unique.
 * nums is an ascending array that is possibly rotated.
 * -10^4 <= target <= 10^4
 * 
 * 
 */

// [3,5,1] target = 3
//  0 1 2 3 4 5 6 7
// [4,5,6,7,0,1,2,3] target = 8
//  l   r   m   rb < lb    t > rb         v > t
//  0   7   3      t         t    

// @lc code=start
function search(nums: number[], target: number): number {
    let left: number = 0;
    let right: number = nums.length - 1;

    while (left <= right) {
        let midIdx: number = Math.floor((left + right) / 2);
        if (nums[midIdx] === target) return midIdx;

        if (nums[left] <= nums[midIdx]) {
            if (nums[left] <= target && target <= nums[midIdx])
                right = midIdx - 1;
            else left = midIdx + 1;
        } else {
            if (nums[midIdx] <= target && target <= nums[right])
                left = midIdx + 1;
            else right = midIdx - 1;
        }
    }
    return -1;
};
// @lc code=end

