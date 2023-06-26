/*
 * @lc app=leetcode id=739 lang=typescript
 *
 * [739] Daily Temperatures
 *
 * https://leetcode.com/problems/daily-temperatures/description/
 *
 * algorithms
 * Medium (67.71%)
 * Likes:    8598
 * Dislikes: 202
 * Total Accepted:    491.5K
 * Total Submissions: 738.5K
 * Testcase Example:  '[73,74,75,71,69,72,76,73]'
 *
 * Given an array of integers temperatures represents the daily temperatures,
 * return an array answer such that answer[i] is the number of days you have to
 * wait after the i^th day to get a warmer temperature. If there is no future
 * day for which this is possible, keep answer[i] == 0 instead.
 * 
 * 
 * Example 1:
 * Input: temperatures = [73,74,75,71,69,72,76,73]
 * Output: [1,1,4,2,1,1,0,0]
 * Example 2:
 * Input: temperatures = [30,40,50,60]
 * Output: [1,1,1,0]
 * Example 3:
 * Input: temperatures = [30,60,90]
 * Output: [1,1,0]
 * 
 * 
 * Constraints:
 * 
 * 
 * 1 <= temperatures.length <= 10^5
 * 30 <= temperatures[i] <= 100
 * 
 * 
 */

// @lc code=start

type tempIndex = {
    temp: number,
    index: number,
}
function dailyTemperatures(temperatures: number[]): number[] {
    const ans = Array(temperatures.length).fill(0);
    const stack : tempIndex[] = []

    temperatures.forEach((val, i) => {
        while (stack.length > 0 && stack[stack.length - 1].temp < val) {
            const { index } = stack.pop()!
            ans[index] = i - index
        }
        stack.push({temp: val, index: i})
    });

    return ans

};
// @lc code=end

