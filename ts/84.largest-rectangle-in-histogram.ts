/*
 * @lc app=leetcode id=84 lang=typescript
 *
 * [84] Largest Rectangle in Histogram
 *
 * https://leetcode.com/problems/largest-rectangle-in-histogram/description/
 *
 * algorithms
 * Hard (42.42%)
 * Likes:    14751
 * Dislikes: 209
 * Total Accepted:    689.9K
 * Total Submissions: 1.6M
 * Testcase Example:  '[2,1,5,6,2,3]'
 *
 * Given an array of integers heights representing the histogram's bar height
 * where the width of each bar is 1, return the area of the largest rectangle
 * in the histogram.
 * 
 * 
 * Example 1:
 * 
 * 
 * Input: heights = [2,1,5,6,2,3]
 * Output: 10
 * Explanation: The above is a histogram where width of each bar is 1.
 * The largest rectangle is shown in the red area, which has an area = 10
 * units.
 * 
 * 
 * Example 2:
 * 
 * 
 * Input: heights = [2,4]
 * Output: 4
 * 
 * 
 * 
 * Constraints:
 * 
 * 
 * 1 <= heights.length <= 10^5
 * 0 <= heights[i] <= 10^4
 * 
 * 
 */

// @lc code=start
function largestRectangleArea(heights: number[]): number {
    heights.push(0)
    const stack: number[] = [-1]
    let area = 0;

    for (let i = 0; i < heights.length; i++) {
        let curHeight = heights[i]
        let lBoundHeight = heights[stack[stack.length - 1]]
        while (curHeight < lBoundHeight) {
            stack.pop()
            let h = lBoundHeight
            let w = i - 1 - stack[stack.length - 1]
            area = Math.max(area, h * w)
            lBoundHeight = heights[stack[stack.length - 1]]
        }
        stack.push(i)
    }
    return area
};
// @lc code=end

