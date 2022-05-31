/*
 * @lc app=leetcode id=121 lang=cpp
 *
 * [121] Best Time to Buy and Sell Stock
 */
#include <vector>
using std::vector;
// @lc code=start
class Solution {
public:
// Accepted
// 211/211 cases passed (146 ms)
// Your runtime beats 78.78 % of cpp submissions
// Your memory usage beats 89.87 % of cpp submissions (93.3 MB)
    int maxProfit(vector<int>& prices) {
		int min = prices[0];
		int profit = 0;
		for (auto i : prices) {
			if (i < min) {
				min = i;
			}
			if (profit < i - min) {
				profit = i - min;
			}
		}
		return profit;
    }
};
// @lc code=end
//** attempt 2 -> time limit exceeded on test 198
    // int maxProfit(vector<int>& prices) {
	// 	if (prices.size() < 2) return 0;
	// 	int largest_diff = 0;
	// 	int min, max;

	// 	for (int i = 0; i < prices.size(); i ++) {
	// 		for (int j = i + 1; j < prices.size(); j++) {
	// 			if (prices[j] - prices[i] > largest_diff) {
	// 				largest_diff = prices[j] - prices [i];
	// 			}
	// 		}
	// 	}
	// 	return largest_diff;
    // }

//** first attempt -> failed test 210
	//int maxProfit(vector<int>& prices) {
	// 	if (prices.size() < 2) return 0;

	// 	int max, max_index, min_b4_max;

	// 	max = prices[1];
	// 	max_index = 1;
	// 	for (int i = 2; i < prices.size(); i ++) {
	// 		if (prices[i] >= max) {
	// 			max = prices[i];
	// 			max_index = i;
	// 		}
	// 	}
        
	// 	min_b4_max = max;
	// 	for (int i = 0; i < max_index; i++) {
	// 		if (prices[i] < min_b4_max) {
	// 			min_b4_max = prices[i];
	// 		}
	// 	}

	// 	int min = prices[0], min_index = 0, max_after_min;
	// 	for (int i = 0; i < prices.size() -1; i++) {
	// 		if (prices[i] < min) {
	// 			min = prices[i];
	// 			min_index = i;
	// 		}
	// 	}
	// 	max_after_min = min;
	// 	for (int i = min_index; i < prices.size() ; i ++) {
	// 		if (prices[i] > max_after_min) {
	// 			max_after_min = prices[i];
	// 		}
	// 	}
		
	// 	if (max_after_min - min > max - min_b4_max){
	// 		return max_after_min - min;
	// 	}
	// 	return max - min_b4_max;

    // }
