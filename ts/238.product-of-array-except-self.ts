/*
 * @lc app=leetcode id=238 lang=typescript
 *
 * [238] Product of Array Except Self
 *
 * https://leetcode.com/problems/product-of-array-except-self/description/
 *
 * algorithms
 * Medium (64.97%)
 * Likes:    17983
 * Dislikes: 989
 * Total Accepted:    1.7M
 * Total Submissions: 2.6M
 * Testcase Example:  '[1,2,3,4]'
 *
 * Given an integer array nums, return an array answer such that answer[i] is
 * equal to the product of all the elements of nums except nums[i].
 * 
 * The product of any prefix or suffix of nums is guaranteed to fit in a 32-bit
 * integer.
 * 
 * You must write an algorithm that runs in O(n) time and without using the
 * division operation.
 * 
 * 
 * Example 1:
 * Input: nums = [1,2,3,4]
 * Output: [24,12,8,6]
 * Example 2:
 * Input: nums = [-1,1,0,-3,3]
 * Output: [0,0,9,0,0]
 * 
 * 
 * Constraints:
 * 
 * 
 * 2 <= nums.length <= 10^5
 * -30 <= nums[i] <= 30
 * The product of any prefix or suffix of nums is guaranteed to fit in a 32-bit
 * integer.
 * 
 * 
 * 
 * Follow up: Can you solve the problem in O(1) extra space complexity? (The
 * output array does not count as extra space for space complexity analysis.)
 * 
 */
// nums: [1, 2, 3, 4]
// prod: [1, 1, 1, 1]
// buff: [1, 1]
// i = 1
// buffer = [1 * 1, 1 * 4]
// prod

// @lc code=start
function productExceptSelf(nums: number[]): number[] {
    let prod = new Array(nums.length).fill(1);
    let prefix = 1;
    let postfix = 1;
    let len = nums.length
    for( let i = 1; i < len; i ++) {
        prefix *= nums[i - 1]
        postfix *= nums[len - i]
        prod[i] *= prefix
        prod[len - i - 1] *= postfix
    }
    return prod
};
// @lc code=end


// function productExceptSelf(nums: number[]): number[] {
//     let products = new Array(nums.length).fill(1);
//     let prefix = 1;
//     for( let i = 0; i < nums.length; i ++) {
//         products[i] = prefix
//         prefix *= nums[i]
//     }
//     let post = 1;
//     for (let i = nums.length - 1; i > -1; i--) {
//         products[i] *= post
//         post *= nums[i]
//     }
//     return products
// };