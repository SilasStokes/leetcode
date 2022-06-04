/*
 * @lc app=leetcode id=704 lang=cpp
 *
 * [704] Binary Search
 */



#include <vector>
using std::vector;
//				   0 1 2 3 4 5 -> len = 6, div by 2 = 3
// Input: nums = [-1,0,3,5,9,12], target = 9
//					
// @lc code=start
class Solution {
public:
    int search(vector<int>& nums, int target) {
		if (target < nums[0] || target > nums[nums.size()-1]) return -1;
		
		if (nums.size() < 3){
			return (nums[0] == target) ? 0 : (nums[1] == target)? 1 : -1;
		}
		int index = (nums.size()-1) / 2 + (nums.size() -1) % 2;
		int lbound = 0, ubound = nums.size() - 1;

		while (nums[index] != target && ubound - lbound > 1) {
			if (nums[index] < target) {
				lbound = index;
				index = index + (ubound - lbound) / 2 + (ubound - lbound) % 2;
				continue;
			}
			if (nums[index] > target) {
				ubound = index;
				index = index - (ubound - lbound) / 2 - (ubound - lbound) % 2;
				continue;
			}
		}
		return (nums[index] == target) ? index : -1;
    }

    int search(vector<int>& nums, int target) {
		int n = nums.size()-1;
        int low = 0, high = n;
        while( low <= high){
            int mid = low + (high-low)/2;
            if (nums[mid] == target) 
				return mid;
            else if (nums[mid] > target) 
				high = mid - 1;
            else 
				low = mid + 1;
        }
        return -1;
	}

};
// @lc code=end


		



		// if (target < nums[0] || target > nums[nums.size()-1]) 
		// 	return - 1;

		// int middle = nums.size() / 2 + nums.size() %2;

		// if (nums[middle] == target) 
		// 	return middle;

		// if (nums[middle + 1] > target && nums[middle-1] < target)
		// 	return -1;

		// if (nums[middle] < target ) { 
		// 	vector<int> v1(nums.begin() + middle + 1, nums.end() );
		// 	return search(v1,target);
		// } else {
		// 	vector<int> v1(nums.begin(), nums.end() - middle );
		// 	return search(v1,target);

		// }
		
        