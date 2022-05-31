/*
 * @lc app=leetcode id=20 lang=cpp
 *
 * [20] Valid Parentheses
 */

#include <string> 
#include <stack> 
using std::string;
// @lc code=start
class Solution {
public:
	// Runtime: 0 ms, faster than 100.00% of C++ online submissions for Valid Parentheses.
	// Memory Usage: 6.2 MB, less than 96.25% of C++ online submissions for Valid Parentheses.

    bool isValid(string s) {
		std::stack<char> stack;
		for(int i = 0; i < s.size(); i++) {
			if (s[i] == '(' || s[i] == '[' || s[i] == '{' ) {
				stack.push(s[i]);
			}
			else {
				if ( 
					stack.empty() ||
					stack.top() == '(' && s[i] != ')' ||
					stack.top() == '[' && s[i] != ']' ||
					stack.top() == '{' && s[i] != '}' 
				) {
					return false;
				}
				stack.pop();
			}
		}
		return stack.empty();
    }
};
// @lc code=end
//hint 1
// An interesting property about a valid parenthesis expression is that a sub-expression of a valid expression should also be a valid expression. (Not every sub-expression) e.g.
// { { } [ ] [ [ [ ] ] ] }  is VALID expression
//           [ [ [ ] ] ]    is VALID sub-expression
//   { } [ ]                is VALID sub-expression
// Can we exploit this recursive structure somehow?

// hint 2
// What if whenever we encounter a matching pair of parenthesis in the expression, we simply remove it from the expression? This would keep on shortening the expression. e.g.
// { { ( { } ) } }
//       |_|
//
// stack -> top 											bottom
// 				{ {

// { { (      ) } }
//     |______|

// { {          } }
//   |__________|

// {                }
// |________________|
// VALID EXPRESSION!

// hint3:
// The stack data structure can come in handy here in representing this recursive 
// structure of the problem. We can't really process this from the inside out 
// because we don't have an idea about the overall structure. But, the stack can 
// help us process this recursively i.e. from outside to inwards.


// first attempt:
//    bool isValid(string s) {
// 		// const char * cp = s.c_str();
// 		int paren = 0, squiggle = 0, bracket = 0;
// 		// while (cp) {
// 		for (int i = 0; i < s.length(); i++){
// 			switch (s[i]){
// 				case '(':
// 					paren++;
// 					break;
// 				case ')':
// 				 	if (paren % 2 != 1 || paren == 0){
// 						 // out of order
// 						return false;
// 					}
// 					paren--;
// 					break;
// 				case '[':
// 					bracket++;
// 					break;
// 				case ']':
// 				 	if (bracket % 2 != 1 || bracket== 0){
// 						return false;
// 					}
// 					bracket--;
// 					break;
// 				case '{':
// 					squiggle++;
// 					break;
// 				case '}':
// 				 	if (squiggle % 2 != 1 || squiggle== 0){
// 						return false;
// 					}
// 					squiggle--;
// 					break;
// 				default:
// 					break;
// 			}
// 		}
// 		return paren == 0 && squiggle == 0 && bracket == 0;
//     }
