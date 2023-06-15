/*
 * @lc app=leetcode id=347 lang=typescript
 *
 * [347] Top K Frequent Elements
 *
 * https://leetcode.com/problems/top-k-frequent-elements/description/
 *
 * algorithms
 * Medium (64.88%)
 * Likes:    11582
 * Dislikes: 428
 * Total Accepted:    1.2M
 * Total Submissions: 1.9M
 * Testcase Example:  '[1,1,1,2,2,3]\n2'
 *
 * Given an integer array nums and an integer k, return the k most frequent
 * elements. You may return the answer in any order.
 * 
 * 
 * Example 1:
 * Input: nums = [1,1,1,2,2,3], k = 2
 * Output: [1,2]
 * Example 2:
 * Input: nums = [1], k = 1
 * Output: [1]
 * 
 * 
 * Constraints:
 * 
 * 
 * 1 <= nums.length <= 10^5
 * -10^4 <= nums[i] <= 10^4
 * k is in the range [1, the number of unique elements in the array].
 * It is guaranteed that the answer is unique.
 * 
 * 
 * 
 * Follow up: Your algorithm's time complexity must be better than O(n log n),
 * where n is the array's size.
 * 
 */

// @lc code=start
function topKFrequent(nums: number[], k: number): number[] {
    const freq = new Map<number, number>();
    for (const n of nums) {
        if (!freq.has(n)) freq.set(n, 0)
        freq.set(n, freq.get(n) + 1)
    }
    return Array.from(freq.entries()).sort((a,b) => b[1] - a[1]).slice(0,k).map( a => a[0])
};

// @lc code=end
// function topKFrequent(nums: number[], k: number): number[] {
//     const freq: {[key: number] : number} = {};
//     for (const n of nums){
//         if (freq[n] === undefined) freq[n] = 0;
//         freq[n] += 1;
//     }

//     return Object.entries(freq)
//         .sort((a,b) => b[1] - a[1]) // n log n > n 
//         .slice(0, k)
//         .map((a) => Number(a[0]))
// };

