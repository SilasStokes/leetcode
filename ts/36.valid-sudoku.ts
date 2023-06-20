/*
 * @lc app=leetcode id=36 lang=typescript
 *
 * [36] Valid Sudoku
 *
 * https://leetcode.com/problems/valid-sudoku/description/
 *
 * algorithms
 * Medium (57.94%)
 * Likes:    8836
 * Dislikes: 923
 * Total Accepted:    1.1M
 * Total Submissions: 1.9M
 * Testcase Example:  '[["5","3",".",".","7",".",".",".","."],["6",".",".","1","9","5",".",".","."],[".","9","8",".",".",".",".","6","."],["8",".",".",".","6",".",".",".","3"],["4",".",".","8",".","3",".",".","1"],["7",".",".",".","2",".",".",".","6"],[".","6",".",".",".",".","2","8","."],[".",".",".","4","1","9",".",".","5"],[".",".",".",".","8",".",".","7","9"]]'
 *
 * Determine if a 9 x 9 Sudoku board is valid. Only the filled cells need to be
 * validated according to the following rules:
 * 
 * 
 * Each row must contain the digits 1-9 without repetition.
 * Each column must contain the digits 1-9 without repetition.
 * Each of the nine 3 x 3 sub-boxes of the grid must contain the digits 1-9
 * without repetition.
 * 
 * 
 * Note:
 * 
 * 
 * A Sudoku board (partially filled) could be valid but is not necessarily
 * solvable.
 * Only the filled cells need to be validated according to the mentioned
 * rules.
 * 
 * 
 * 
 * Example 1:
 * 
 * 
 * Input: board = 
 * [["5","3",".",".","7",".",".",".","."]
 * ,["6",".",".","1","9","5",".",".","."]
 * ,[".","9","8",".",".",".",".","6","."]
 * ,["8",".",".",".","6",".",".",".","3"]
 * ,["4",".",".","8",".","3",".",".","1"]
 * ,["7",".",".",".","2",".",".",".","6"]
 * ,[".","6",".",".",".",".","2","8","."]
 * ,[".",".",".","4","1","9",".",".","5"]
 * ,[".",".",".",".","8",".",".","7","9"]]
 * Output: true
 * 
 * 
 * Example 2:
 * 
 * 
 * Input: board = 
 * [["8","3",".",".","7",".",".",".","."]
 * ,["6",".",".","1","9","5",".",".","."]
 * ,[".","9","8",".",".",".",".","6","."]
 * ,["8",".",".",".","6",".",".",".","3"]
 * ,["4",".",".","8",".","3",".",".","1"]
 * ,["7",".",".",".","2",".",".",".","6"]
 * ,[".","6",".",".",".",".","2","8","."]
 * ,[".",".",".","4","1","9",".",".","5"]
 * ,[".",".",".",".","8",".",".","7","9"]]
 * Output: false
 * Explanation: Same as Example 1, except with the 5 in the top left corner
 * being modified to 8. Since there are two 8's in the top left 3x3 sub-box, it
 * is invalid.
 * 
 * 
 * 
 * Constraints:
 * 
 * 
 * board.length == 9
 * board[i].length == 9
 * board[i][j] is a digit 1-9 or '.'.
 * 
 * 
 */

// @lc code=start
function isValidSudoku(board: string[][]): boolean {

    const set = new Set<string>();

    // checking all 9 boxes:
    for (let boxI = 0; boxI < 9; boxI += 3) {
        for (let boxJ = 0; boxJ < 9; boxJ += 3) {
            for (let i = boxI; i < boxI + 3; i++) {
                for (let j = boxJ; j < boxJ + 3; j++) {
                    const val = board[i][j]
                    if (val === '.') {
                        continue
                    }
                    if (set.has(val)) {
                        console.log(`returning false: coordinates = [${i}, ${j}], set =`)
                        console.log(set)
                        return false
                    }
                    set.add(val)
                }
            }
            set.clear()
        }
    }
    set.clear()
    // checking each row:
    for (let i = 0; i < 9; i++) {
        for (let j = 0; j < 9; j++) {
            const val = board[i][j]
            if (val === '.') {
                continue
            }
            if (set.has(val)) {
                console.log(`returning false: coordinates = [${i}, ${j}], set =`)
                console.log(set)
                return false
            }
            set.add(val)
        }
        set.clear()
    }
    set.clear()
    //checking each column
    for (let i = 0; i < 9; i++) {
        for (let j = 0; j < 9; j++) {
            const val = board[j][i]
            if (val === '.') {
                continue
            }
            if (set.has(val)) {
                console.log(`returning false: coordinates = [${i}, ${j}], set =`)
                console.log(set)
                return false
            }
            set.add(val)
        }
        set.clear()
    }

    return true


};
// @lc code=end

