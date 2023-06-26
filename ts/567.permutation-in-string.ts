/*
 * @lc app=leetcode id=567 lang=typescript
 *
 * [567] Permutation in String
 *
 * https://leetcode.com/problems/permutation-in-string/description/
 *
 * algorithms
 * Medium (44.05%)
 * Likes:    7523
 * Dislikes: 250
 * Total Accepted:    508.1K
 * Total Submissions: 1.2M
 * Testcase Example:  '"ab"\n"eidbaooo"'
 *
 * Given two strings s1 and s2, return true if s2 contains a permutation of s1,
 * or false otherwise.
 * 
 * In other words, return true if one of s1's permutations is the substring of
 * s2.
 * 
 * 
 * Example 1:
 * 
 * 
 * Input: s1 = "ab", s2 = "eidbaooo"
 * Output: true
 * Explanation: s2 contains one permutation of s1 ("ba").
 * 
 * 
 * Example 2:
 * 
 * 
 * Input: s1 = "ab", s2 = "eidboaoo"
 * Output: false
 * 
 * 
 * 
 * Constraints:
 * 
 * 
 * 1 <= s1.length, s2.length <= 10^4
 * s1 and s2 consist of lowercase English letters.
 * 
 * 
 */

// @lc code=start
function checkInclusion(s1: string, s2: string): boolean {
    const hash1 = Array(26).fill(0);
    const hash2 = Array (26).fill(0);
    for (let c of s1) {
        hash1[c.charCodeAt(0) - 'a'.charCodeAt(0)]++;
    }
    let l = 0, r = 0;
    let matches = 0;
    const len = s2.length
    while(r < s1.length) {
        const c = s2[r]
        hash2[c.charCodeAt(0) - c.charCodeAt(0)]++
        r++;
    }
    for (let i = 0; i < 26; i++){
        if (hash1[i] === hash2[i]) matches++;
    }
    while(r < len) {
        if (matches === 26) return true;
        const c = s2[r]
        hash2[c.charCodeAt(0) - 'a'.charCodeAt(0)]++;
    }
    return false;
};
// @lc code=end

