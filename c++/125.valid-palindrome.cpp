/*
 * @lc app=leetcode id=125 lang=cpp
 *
 * [125] Valid Palindrome
 */
#include <string>
using std::string;

// @lc code=start
class Solution {
public:
// Runtime: 3 ms, faster than 95.05% of C++ online submissions for Valid Palindrome.
// Memory Usage: 7.2 MB, less than 98.36% of C++ online submissions for Valid Palindrome.
    bool isPalindrome(string s) {
		if (s.empty()) 
			return true;

		int i = 0, j = s.size() -1;
		while (j - i > 0) {
			if (!isalnum(s[i])) {
				i++;
				continue;
			}
			if (!isalnum(s[j])) {
				j--;
				continue;
			}
			// char ti = (isupper(s[i])) ? (char) ( (int) s[i] + 32 ) : s[i];
			// char tj = (isupper(s[j])) ? (char) ( (int) s[j] + 32 ) : s[j];
			if (tolower(s[j]) != tolower(s[i]) ) 
                return false;
            i++; j--;
		}
		return true;
    }
};

// @lc code=end

// first solution:
	// bool isNum(const char c) {
	// 	return (int)c >= (int) '0' && (int)c <= (int) '9' ;
	// }

	// bool isPalindrome(string s) {
	// 	for(int i = 0; i < s.size(); i++) {
	// 		if (isupper(s[i])) {
	// 			//                                    97 - 65
	// 			s[i] = (char) ( (int) s[i] + ( (int) 'a' - (int) 'A' ) );
	// 		}
	// 		else if (  !isNum(s[i]) && !islower(s[i]) ) 
	// 		{
	// 			s.erase(i, 1);
	// 			i--;
	// 		}
	// 	}

	// 	if (s.empty()) 
	// 		return true;

	// 	for (int i = 0, j = s.size() - 1; j - i > 0 ; i++, j--) {
	// 		if (s[i] != s[j]) return false;
	// 	}
	// 	return true;
	// }

