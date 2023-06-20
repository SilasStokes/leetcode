/*
 * @lc app=leetcode id=125 lang=typescript
 *
 * [125] Valid Palindrome
 *
 * https://leetcode.com/problems/valid-palindrome/description/
 *
 * algorithms
 * Easy (42.97%)
 * Likes:    5262
 * Dislikes: 6232
 * Total Accepted:    1.6M
 * Total Submissions: 3.8M
 * Testcase Example:  '"A man, a plan, a canal: Panama"'
 *
 * A phrase is a palindrome if, after converting all uppercase letters into
 * lowercase letters and removing all non-alphanumeric characters, it reads the
 * same forward and backward. Alphanumeric characters include letters and
 * numbers.
 * 
 * Given a string s, return true if it is a palindrome, or false otherwise.
 * 
 * 
 * Example 1:
 * 
 * 
 * Input: s = "A man, a plan, a canal: Panama"
 * Output: true
 * Explanation: "amanaplanacanalpanama" is a palindrome.
 * 
 * 
 * Example 2:
 * 
 * 
 * Input: s = "race a car"
 * Output: false
 * Explanation: "raceacar" is not a palindrome.
 * 
 * 
 * Example 3:
 * 
 * 
 * Input: s = " "
 * Output: true
 * Explanation: s is an empty string "" after removing non-alphanumeric
 * characters.
 * Since an empty string reads the same forward and backward, it is a
 * palindrome.
 * 
 * 
 * 
 * Constraints:
 * 
 * 
 * 1 <= s.length <= 2 * 10^5
 * s consists only of printable ASCII characters.
 * 
 * 
 */



// @lc code=start
function isPalindrome(s: string): boolean {
    const aCharCode = 'a'.charCodeAt(0);
    const zCharCode = 'z'.charCodeAt(0);
    const zeroCharCode = '0'.charCodeAt(0);
    const nineCharCode = '9'.charCodeAt(0);
    function isAlphaNumeric(index:number) {
        const c = s.charAt(index).charCodeAt(0)
        return ( (c >= aCharCode && c <= zCharCode ) || (c >= zeroCharCode && c <= nineCharCode) )
    }
    s = s.toLocaleLowerCase()
    let l = 0, r = s.length - 1;
    while (l < r) {
        while ( l < r && !isAlphaNumeric(l)) {
            l++;
        }
        while ( l < r && !isAlphaNumeric(r)) {
            r--;
        }
        if (s[l] !== s[r]) {
            return false;
        }
        l++;
        r--;

    }
    return true;

};
// @lc code=end

