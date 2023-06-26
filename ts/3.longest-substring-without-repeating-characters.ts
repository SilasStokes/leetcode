/*
 * @lc app=leetcode id=3 lang=typescript
 *
 * [3] Longest Substring Without Repeating Characters
 *
 * https://leetcode.com/problems/longest-substring-without-repeating-characters/description/
 *
 * algorithms
 * Medium (33.63%)
 * Likes:    30158
 * Dislikes: 1290
 * Total Accepted:    4M
 * Total Submissions: 11.9M
 * Testcase Example:  '"abcabcbb"'
 *
 * Given a string s, find the length of the longest substring without repeating
 * characters.
 * 
 * 
 * Example 1:
 * 
 * 
 * Input: s = "abcabcbb"
 * Output: 3
 * Explanation: The answer is "abc", with the length of 3.
 * 
 * 
 * Example 2:
 * 
 * 
 * Input: s = "bbbbb"
 * Output: 1
 * Explanation: The answer is "b", with the length of 1.
 * 
 * 
 * Example 3:
 * 
 * 
 * Input: s = "pwwkew"
 * Output: 3
 * Explanation: The answer is "wke", with the length of 3.
 * Notice that the answer must be a substring, "pwke" is a subsequence and not
 * a substring.
 * 
 * 
 * 
 * Constraints:
 * 
 * 
 * 0 <= s.length <= 5 * 10^4
 * s consists of English letters, digits, symbols and spaces.
 * 
 * 
 */
// "abcabcbb"
//  l  r
// "dvdf"
//  l r

// @lc code=start
function lengthOfLongestSubstring(s: string): number {
    let sol = 0;
    if (s.length === 0) return 0;

    const set = new Set<string>();
    const len = s.length
    let l = 0, r = 0;
    while (r < len) {
        const c = s[r]
        while (set.has(c)) {
            set.delete(s[l])
            l++;
        }
        // if (set.has(c)) {
        //     while(s[l] !== c) {
        //         set.delete(s[l])
        //         l++
        //     }
        //     set.delete(s[l])
        //     l++;
        // }
        set.add(c)
        r++;
        sol = Math.max(sol, r - l)
    }
    return sol;

};
// @lc code=end

