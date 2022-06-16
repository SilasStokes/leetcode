/*
 * @lc app=leetcode id=235 lang=cpp
 *
 * [235] Lowest Common Ancestor of a Binary Search Tree
 */

// Definition for a binary tree node.
#define NULL nullptr
struct TreeNode {
    int val;
    TreeNode *left;
    TreeNode *right;
    TreeNode(int x) : val(x), left(NULL), right(NULL) {}
};

#include <stack>

// @lc code=start
/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     TreeNode *left;
 *     TreeNode *right;
 *     TreeNode(int x) : val(x), left(NULL), right(NULL) {}
 * };
 */

class Solution {
public:
	TreeNode * LCA_helper(std::stack<TreeNode *> *& s, TreeNode * root, int val) {

		if (root == nullptr) return root;
		if(root -> val == val) {
			return root;
		}
		s->push(root);

		TreeNode * temp = LCA_helper(s, root -> left, val);
		if (temp == nullptr)
			LCA_helper(s, root -> right, val);

		s-> pop();

	}

    TreeNode* lowestCommonAncestor(TreeNode* root, TreeNode* p, TreeNode* q) {
		std::stack<TreeNode *> ppath;
		std::stack<TreeNode *> qpath;

		TreeNode * temp = root;
		ppath.push(temp);
		while (temp -> val != p -> val) {
			temp = ppath.top();
			ppath.pop();
			ppath.push(temp -> left);
			ppath.push(temp -> right);
		}

    }
};
// @lc code=end

