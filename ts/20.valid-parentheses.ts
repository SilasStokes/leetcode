/*
 * @lc app=leetcode id=20 lang=typescript
 *
 * [20] Valid Parentheses
 *
 * https://leetcode.com/problems/valid-parentheses/description/
 *
 * algorithms
 * Easy (40.79%)
 * Likes:    16680
 * Dislikes: 856
 * Total Accepted:    2.8M
 * Total Submissions: 6.9M
 * Testcase Example:  '"()"'
 *
 * Given a string s containing just the characters '(', ')', '{', '}', '[' and
 * ']', determine if the input string is valid.
 * 
 * An input string is valid if:
 * 
 * 
 * Open brackets must be closed by the same type of brackets.
 * Open brackets must be closed in the correct order.
 * Every close bracket has a corresponding open bracket of the same type.
 * 
 * 
 * 
 * Example 1:
 * 
 * 
 * Input: s = "()"
 * Output: true
 * 
 * 
 * Example 2:
 * 
 * 
 * Input: s = "()[]{}"
 * Output: true
 * 
 * 
 * Example 3:
 * 
 * 
 * Input: s = "(]"
 * Output: false
 * 
 * 
 * 
 * Constraints:
 * 
 * 
 * 1 <= s.length <= 10^4
 * s consists of parentheses only '()[]{}'.
 * 
 * 
 */

// @lc code=start
function isValid(s: string): boolean {
    const stack: string[] = [];
    const map = {
        '[': ']',
        '{': '}',
        '(': ')'
    }

    for (let c of s) {
        if (c in map) {
            stack.push(c)
        } else {
            const b = stack.pop();
            if (b === 'undefined' || map[b!] !== c) return false;
        }
    }
    return stack.length === 0;

};
// @lc code=end

