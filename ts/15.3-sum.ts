/*
 * @lc app=leetcode id=15 lang=typescript
 *
 * [15] 3Sum
 *
 * https://leetcode.com/problems/3sum/description/
 *
 * algorithms
 * Medium (31.89%)
 * Likes:    22450
 * Dislikes: 2049
 * Total Accepted:    2.4M
 * Total Submissions: 7.3M
 * Testcase Example:  '[-1,0,1,2,-1,-4]'
 *
 * Given an integer array nums, return all the triplets [nums[i], nums[j],
 * nums[k]] such that i != j, i != k, and j != k, and nums[i] + nums[j] +
 * nums[k] == 0.
 * 
 * Notice that the solution set must not contain duplicate triplets.
 * 
 * 
 * Example 1:
 * 
 * 
 * Input: nums = [-1,0,1,2,-1,-4]
 * Output: [[-1,-1,2],[-1,0,1]]
 * Explanation: 
 * nums[0] + nums[1] + nums[2] = (-1) + 0 + 1 = 0.
 * nums[1] + nums[2] + nums[4] = 0 + 1 + (-1) = 0.
 * nums[0] + nums[3] + nums[4] = (-1) + 2 + (-1) = 0.
 * The distinct triplets are [-1,0,1] and [-1,-1,2].
 * Notice that the order of the output and the order of the triplets does not
 * matter.
 * 
 * 
 * Example 2:
 * 
 * 
 * Input: nums = [0,1,1]
 * Output: []
 * Explanation: The only possible triplet does not sum up to 0.
 * 
 * 
 * Example 3:
 * 
 * 
 * Input: nums = [0,0,0]
 * Output: [[0,0,0]]
 * Explanation: The only possible triplet sums up to 0.
 * 
 * 
 * 
 * Constraints:
 * 
 * 
 * 3 <= nums.length <= 3000
 * -10^5 <= nums[i] <= 10^5
 * 
 * 
 */

// @lc code=start
function threeSum(nums: number[]): number[][] {
    const sol: number[][] = [];
    nums.sort((a, b) => a - b); //  [-1,0,1,2,-1,-4] -> [-4, -1, -1, 0, 1, 2]
    let duplicateTracker: number = 0;
    for (let i = 0; i < nums.length - 2 /* bc i, j and k  */; i++) {
        const target = nums[i];
        if (target > 0) break
        if (i > 0 && target === duplicateTracker) continue

        let l = i + 1, r = nums.length - 1;
        let lDup = 0, rDup = 0;
        while (l < r) {
            const sum = nums[l] + nums[r];
            if (sum + target === 0) {
                sol.push([nums[i], nums[l], nums[r]])
            }
            if (sum + target > 0) {
                let lastVal = nums[r];
                while (nums[r] === lastVal) r--;
            }
            else {
                let lastVal = nums[l];
                while (nums[l] === lastVal) l++;
            }
        }
        duplicateTracker = target
    }

    return sol
};
// @lc code=end

