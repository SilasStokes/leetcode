/*
 * @lc app=leetcode id=74 lang=typescript
 *
 * [74] Search a 2D Matrix
 *
 * https://leetcode.com/problems/search-a-2d-matrix/description/
 *
 * algorithms
 * Medium (46.15%)
 * Likes:    10436
 * Dislikes: 316
 * Total Accepted:    1M
 * Total Submissions: 2.2M
 * Testcase Example:  '[[1,3,5,7],[10,11,16,20],[23,30,34,60]]\n3'
 *
 * Write an efficient algorithm that searches for a value target in an m x n
 * integer matrix matrix. This matrix has the following properties:
 * 
 * 
 * Integers in each row are sorted from left to right.
 * The first integer of each row is greater than the last integer of the
 * previous row.
 * 
 * 
 * 
 * Example 1:
 * 
 * 
 * Input: matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]], target = 3
 * Output: true
 * 
 * 
 * Example 2:
 * 
 * 
 * Input: matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]], target = 13
 * Output: false
 * 
 * 
 * 
 * Constraints:
 * 
 * 
 * m == matrix.length
 * n == matrix[i].length
 * 1 <= m, n <= 100
 * -10^4 <= matrix[i][j], target <= 10^4
 * 
 * 
 */

// @lc code=start
function searchMatrix(matrix: number[][], target: number): boolean {

    let l = 0, r = matrix.length - 1;
    let row: number[] | null = null;
    while (l <= r) {
        const mid = Math.floor((r - l )/ 2) + l
        if (target >= matrix[mid][0] && target <= matrix[mid][matrix[mid].length - 1] ){
            row = matrix[mid]
            break
        }

        if ( target > matrix[mid][matrix[mid].length - 1] ) {
            l = mid + 1;
        } else {
            r = mid - 1;
        }
    }
    if (row === null) return false;

    l = 0, r = row!.length - 1;
    while (l <= r) {
        const mid = Math.floor((r - l) / 2) + l

        if (target === row![mid]) {
            return true;
        }
        if (target > row![mid]) {
            l = mid + 1;
        } else{
            r = mid -1;
        }
    }
    return false;
};
// @lc code=end

