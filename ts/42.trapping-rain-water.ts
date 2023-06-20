/*
 * @lc app=leetcode id=42 lang=typescript
 *
 * [42] Trapping Rain Water
 *
 * https://leetcode.com/problems/trapping-rain-water/description/
 *
 * algorithms
 * Hard (59.10%)
 * Likes:    27061
 * Dislikes: 372
 * Total Accepted:    1.6M
 * Total Submissions: 2.6M
 * Testcase Example:  '[0,1,0,2,1,0,1,3,2,1,2,1]'
 *
 * Given n non-negative integers representing an elevation map where the width
 * of each bar is 1, compute how much water it can trap after raining.
 * 
 * 
 * Example 1:
 * 
 * 
 * Input: height = [0,1,0,2,1,0,1,3,2,1,2,1]
 * Output: 6
 * Explanation: The above elevation map (black section) is represented by array
 * [0,1,0,2,1,0,1,3,2,1,2,1]. In this case, 6 units of rain water (blue
 * section) are being trapped.
 * 
 * 
 * Example 2:
 * 
 * 
 * Input: height = [4,2,0,3,2,5]
 * Output: 9
 * 
 * 
 * 
 * Constraints:
 * 
 * 
 * n == height.length
 * 1 <= n <= 2 * 10^4
 * 0 <= height[i] <= 10^5
 * 
 * 
 */

// @lc code=start
function trap(height: number[]): number {
    let sum: number = 0;
    let l = 0, r = height.length - 1;
    let leftMax = height[l], rightMax =  height[r];

    while (l < r) {
        if (leftMax < rightMax) {
            l++;
            leftMax = Math.max(leftMax, height[l])
            sum = sum + leftMax - height[l]
        } else {
            r--;
            rightMax = Math.max(rightMax, height[r])
            sum = sum + rightMax - height[r]
        }
    }
    return sum;
};
// @lc code=end

