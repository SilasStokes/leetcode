/*
 * @lc app=leetcode id=424 lang=typescript
 *
 * [424] Longest Repeating Character Replacement
 *
 * https://leetcode.com/problems/longest-repeating-character-replacement/description/
 *
 * algorithms
 * Medium (51.24%)
 * Likes:    6611
 * Dislikes: 257
 * Total Accepted:    361.1K
 * Total Submissions: 702.1K
 * Testcase Example:  '"ABAB"\n2'
 *
 * You are given a string s and an integer k. You can choose any character of
 * the string and change it to any other uppercase English character. You can
 * perform this operation at most k times.
 * 
 * Return the length of the longest substring containing the same letter you
 * can get after performing the above operations.
 * 
 * 
 * Example 1:
 * 
 * 
 * Input: s = "ABAB", k = 2
 * Output: 4
 * Explanation: Replace the two 'A's with two 'B's or vice versa.
 * 
 * 
 * Example 2:
 * 
 * 
 * Input: s = "AABABBA", k = 1
 * Output: 4
 * Explanation: Replace the one 'A' in the middle with 'B' and form "AABBBBA".
 * The substring "BBBB" has the longest repeating letters, which is 4.
 * 
 * 
 * 
 * Constraints:
 * 
 * 
 * 1 <= s.length <= 10^5
 * s consists of only uppercase English letters.
 * 0 <= k <= s.length
 * 
 * 
 */

// @lc code=start
function characterReplacement(s: string, k: number): number {
    let maxf = 0;
    let l = 0, r = 0;
    let maxLength = 0;

    const len = s.length
    const count = new Map<string, number>();
    while (r < len) {
        const c = s[r]
        if (!count.has(c)) {
            count.set(c, 0)
        }
        const curCount = count.get(c)! + 1;

        count.set(c, curCount)
        maxf = Math.max(maxf, curCount)

        const curLength = r - l + 1;
        if (curLength - maxf > k) {
            const lc = s[l]
            count.set(lc, count.get(lc)! - 1)
            l++;
        }
        maxLength = Math.max(maxLength, r - l + 1)
        r++;
    }
    return maxLength;
};
// @lc code=end

