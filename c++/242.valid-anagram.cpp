/*
 * @lc app=leetcode id=242 lang=cpp
 *
 * [242] Valid Anagram
 */
#include <string>
using std::string;

// @lc code=start
class Solution {
public:

	// something like this, will probably come back for this solution:
	// rn failes test 35. 
    // bool isAnagram(string s, string t) {
	// 	// lets do a random hash(?)
	//   	if (s.size() != t.size()) return false;
	// 	int sHash = 0;
	// 	int tHash = 0;
	// 	for (int i = 0; i < s.size(); i++) {
	// 		sHash = sHash + s[i] * s[i] ;
	// 		tHash = tHash + t[i] * t[i] ;
	// 	}
	// 	return sHash == tHash;
    // }

// Accepted
// 36/36 cases passed (3 ms)
// Your runtime beats 98.44 % of cpp submissions
// Your memory usage beats 8.71 % of cpp submissions (7.4 MB)
	#define ALPHABET_LENGTH 26
    bool isAnagram(string s, string t) {
	 	if (s.size() != t.size()) return false;
		int count[ALPHABET_LENGTH] = {0};
		for (int i = 0; i < s.size(); i++){
			count[s[i] - (int)'a']++;
			count[t[i] - (int)'a']--;
		}
		for (auto i : count) {
			if (i) return false;
		}
		return true;
    }
// Accepted
// 36/36 cases passed (863 ms)
// Your runtime beats 5.01 % of cpp submissions
// Your memory usage beats 46.76 % of cpp submissions (7.3 MB)
    // bool isAnagram(string s, string t) {
	// 	if (s.size() != t.size()) return false;
	// 	// dumb solution:
	// 	for (auto i:s){
	// 		size_t index = t.find_first_of(i);
	// 		if (index == -1) return false;
	// 		t.erase(index, 1);
	// 	}
	// 	return t.empty();
    // }
};
// @lc code=end

