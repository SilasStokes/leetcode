/*
 * @lc app=leetcode id=11 lang=typescript
 *
 * [11] Container With Most Water
 *
 * https://leetcode.com/problems/container-with-most-water/description/
 *
 * algorithms
 * Medium (54.12%)
 * Likes:    21139
 * Dislikes: 1125
 * Total Accepted:    1.8M
 * Total Submissions: 3.4M
 * Testcase Example:  '[1,8,6,2,5,4,8,3,7]'
 *
 * You are given an integer array height of length n. There are n vertical
 * lines drawn such that the two endpoints of the i^th line are (i, 0) and (i,
 * height[i]).
 * 
 * Find two lines that together with the x-axis form a container, such that the
 * container contains the most water.
 * 
 * Return the maximum amount of water a container can store.
 * 
 * Notice that you may not slant the container.
 * 
 * 
 * Example 1:
 * 
 * 
 * Input: height = [1,8,6,2,5,4,8,3,7]
 * Output: 49
 * Explanation: The above vertical lines are represented by array
 * [1,8,6,2,5,4,8,3,7]. In this case, the max area of water (blue section) the
 * container can contain is 49.
 * 
 * 
 * Example 2:
 * 
 * 
 * Input: height = [1,1]
 * Output: 1
 * 
 * 
 * 
 * Constraints:
 * 
 * 
 * n == height.length
 * 2 <= n <= 10^5
 * 0 <= height[i] <= 10^4
 * 
 * 
 */

// @lc code=start
function maxArea(height: number[]): number {
    // the function for max area is (r-l) * Math.min(height[r], height[l])
    let area: number = 0;
    let l = 0, r = height.length - 1;
    while (l < r){
        const minHeight = Math.min(height[l], height[r])
        area = Math.max(area, (r - l ) * minHeight);

        if (minHeight === height[l]) {
            l++;
        } else{
            r--;
        }

    }
    return area;

};
// @lc code=end

