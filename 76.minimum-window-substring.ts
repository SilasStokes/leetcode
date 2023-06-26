/*
 * @lc app=leetcode id=76 lang=typescript
 *
 * [76] Minimum Window Substring
 *
 * https://leetcode.com/problems/minimum-window-substring/description/
 *
 * algorithms
 * Hard (40.82%)
 * Likes:    15248
 * Dislikes: 640
 * Total Accepted:    1M
 * Total Submissions: 2.5M
 * Testcase Example:  '"ADOBECODEBANC"\n"ABC"'
 *
 * Given two strings s and t of lengths m and n respectively, return the
 * minimum window substring of s such that every character in t (including
 * duplicates) is included in the window. If there is no such substring, return
 * the empty string "".
 * 
 * The testcases will be generated such that the answer is unique.
 * 
 * 
 * Example 1:
 * 
 * 
 * Input: s = "ADOBECODEBANC", t = "ABC"
 * Output: "BANC"
 * Explanation: The minimum window substring "BANC" includes 'A', 'B', and 'C'
 * from string t.
 * 
 * 
 * Example 2:
 * 
 * 
 * Input: s = "a", t = "a"
 * Output: "a"
 * Explanation: The entire string s is the minimum window.
 * 
 * 
 * Example 3:
 * 
 * 
 * Input: s = "a", t = "aa"
 * Output: ""
 * Explanation: Both 'a's from t must be included in the window.
 * Since the largest window of s only has one 'a', return empty string.
 * 
 * 
 * 
 * Constraints:
 * 
 * 
 * m == s.length
 * n == t.length
 * 1 <= m, n <= 10^5
 * s and t consist of uppercase and lowercase English letters.
 * 
 * 
 * 
 * Follow up: Could you find an algorithm that runs in O(m + n) time?
 * 
 */

// @lc code=start
function minWindow(s: string, t: string): string {
    if (t.length === 0) return "";

    let matches = 0, needed = t.length;
    const sLength = s.length
    let l = 0, r = 0;
    const tCount = new Map<string, number>();
    const window = new Map<string, number>();
    while (r < needed) {
        let c = t[r]
        if (!tCount.has(c)) {
            tCount.set(c, 0)
        }
        tCount.set(c, tCount.get(c)! + 1)
        r++;
    }
    r = 0;
    let resLen = sLength + 1; // bc this is the max
    let res = [-1, -1]

    while (r < sLength) {
        let c = s[r];

        if (!window.has(c)) window.set(c, 0);

        window.set(c, tCount.get(c)! + 1)

        if (tCount.has(c) && window.get(c) === tCount.get(c)) matches++;

        while (matches === needed) {
            const curLen = r - l + 1
            if (curLen < resLen) {
                res = [l, r]
                resLen = curLen

            }
            const lc = s[l]
            window.set(lc, window.get(lc)! - 1);
            if (tCount.has(lc) && window.get(lc)! < tCount.get(lc)!) matches--;
            l++;
        }

        r++;
    }
    [l, r] = res

    return (resLen !== sLength + 1) ? s.substring(l, r + 1) : "";
};
// @lc code=end

