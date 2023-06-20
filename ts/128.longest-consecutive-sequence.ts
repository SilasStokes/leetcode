/*
 * @lc app=leetcode id=128 lang=typescript
 *
 * [128] Longest Consecutive Sequence
 *
 * https://leetcode.com/problems/longest-consecutive-sequence/description/
 *
 * algorithms
 * Medium (48.67%)
 * Likes:    16553
 * Dislikes: 697
 * Total Accepted:    1.2M
 * Total Submissions: 2.4M
 * Testcase Example:  '[100,4,200,1,3,2]'
 *
 * Given an unsorted array of integers nums, return the length of the longest
 * consecutive elements sequence.
 * 
 * You must write an algorithm that runs in O(n) time.
 * 
 * 
 * Example 1:
 * 
 * 
 * Input: nums = [100,4,200,1,3,2]
 * Output: 4
 * Explanation: The longest consecutive elements sequence is [1, 2, 3, 4].
 * Therefore its length is 4.
 * 
 * 
 * Example 2:
 * 
 * 
 * Input: nums = [0,3,7,2,5,8,4,6,0,1]
 * Output: 9
 * 
 * 
 * 
 * Constraints:
 * 
 * 
 * 0 <= nums.length <= 10^5
 * -10^9 <= nums[i] <= 10^9
 * 
 * 
 */

// @lc code=start
function longestConsecutive(nums: number[]): number {
    let longestSequence = 0;
    let tempCount = 0;
    const set = new Set(nums);

    for (let n of nums) {
        if (!set.has(n - 1)) {
            let temp = n;
            while (set.has(temp++)) {
                tempCount++;
                longestSequence = Math.max(tempCount, longestSequence)
            }
            tempCount = 0;
        }
    }
    return longestSequence;
};
// @lc code=end

