/*
 * @lc app=leetcode id=53 lang=cpp
 *
 * [53] Maximum Subarray
 */
#include <vector>
#include <algorithm>
using std::vector;

// @lc code=start
class Solution {
public:

// Accepted
// 209/209 cases passed (181 ms)
// Your runtime beats 23.15 % of cpp submissions
// Your memory usage beats 11.64 % of cpp submissions (67.8 MB)
    int maxSubArray(vector<int>& nums) {
		int sum = nums[0], max = nums[0];
		for (int i = 1; i < nums.size(); i++) {
			sum = std::max(nums[i], nums[i] + sum);
			if (sum > max) {
				max = sum;
			}
		}
		return max;
	}

	// Accepted
	// 209/209 cases passed (138 ms)
	// Your runtime beats 59.49 % of cpp submissions
	// Your memory usage beats 6.25 % of cpp submissions (74.5 MB)

	// int getMax(int a, int b){
	// 	return (a > b) ? a : b;
	// }

    // int maxSubArray(vector<int>& nums) {
	// 	vector<int> sum;
	// 	sum.push_back(nums[0]);
	// 	int max = sum[0]; 

	// 	for (int i = 1; i < nums.size(); i ++) {
	// 		sum.push_back(getMax(nums[i], nums[i] + sum[i-1]));
	// 		if (max < sum[i]) {
	// 			max = sum[i];
	// 		}
	// 	}
	// 	return max;
    // }
};
// @lc code=end

