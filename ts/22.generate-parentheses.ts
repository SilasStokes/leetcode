/*
 * @lc app=leetcode id=22 lang=typescript
 *
 * [22] Generate Parentheses
 *
 * https://leetcode.com/problems/generate-parentheses/description/
 *
 * algorithms
 * Medium (71.28%)
 * Likes:    15916
 * Dislikes: 612
 * Total Accepted:    1.3M
 * Total Submissions: 1.7M
 * Testcase Example:  '3'
 *
 * Given n pairs of parentheses, write a function to generate all combinations
 * of well-formed parentheses.
 * 
 * 
 * Example 1:
 * Input: n = 3
 * Output: ["((()))","(()())","(())()","()(())","()()()"]
 * Example 2:
 * Input: n = 1
 * Output: ["()"]
 * 
 * 
 * Constraints:
 * 
 * 
 * 1 <= n <= 8
 * 
 * 
 */

// @lc code=start
function generateParenthesis(n: number): string[] {
    const output: string[] = [];
    const stack: string[] = [];
    // stack.push('(')
    function backtrack(open: number, close: number) {
        if(open === n && close === n) {
            output.push(stack.join(''))
            return
        }

        if (open < n) {
            stack.push('(')
            backtrack(open + 1, close )
            stack.pop()
        }

        if (close < open) {
            stack.push(')')
            backtrack(open, close + 1)
            stack.pop()
        }
    }
    backtrack(0, 0)
    return output
};
// @lc code=end

