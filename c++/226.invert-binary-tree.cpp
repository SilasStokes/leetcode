/*
 * @lc app=leetcode id=226 lang=cpp
 *
 * [226] Invert Binary Tree
 */

// @lc code=start
/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     TreeNode *left;
 *     TreeNode *right;
 *     TreeNode() : val(0), left(nullptr), right(nullptr) {}
 *     TreeNode(int x) : val(x), left(nullptr), right(nullptr) {}
 *     TreeNode(int x, TreeNode *left, TreeNode *right) : val(x), left(left), right(right) {}
 * };
 */
#include <stack>

// Accepted
// 77/77 cases passed (8 ms)
// Your runtime beats 12.36 % of cpp submissions
// Your memory usage beats 5.93 % of cpp submissions (9.8 MB)
class Solution {
public:
    TreeNode* invertTree(TreeNode* root) {
		if (root == nullptr)
			return root;
		invertTree(root -> left);
		invertTree(root -> right);
		TreeNode* tempL = root -> left;
		root -> left = root -> right;
		root -> right = tempL;
        return root;
    }
};
// @lc code=end

