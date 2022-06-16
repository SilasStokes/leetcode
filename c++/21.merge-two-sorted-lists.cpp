/*
 * @lc app=leetcode id=21 lang=cpp
 *
 * [21] Merge Two Sorted Lists
 */
struct ListNode {
	int val;
	ListNode *next;
	ListNode() : val(0), next(nullptr) {}
	ListNode(int x) : val(x), next(nullptr) {}
	ListNode(int x, ListNode *next) : val(x), next(next) {}
};



// @lc code=start
/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     ListNode *next;
 *     ListNode() : val(0), next(nullptr) {}
 *     ListNode(int x) : val(x), next(nullptr) {}
 *     ListNode(int x, ListNode *next) : val(x), next(next) {}
 * };
 */
class Solution {
public:
	// time : O(n)
	// space: O(1)
	// 208/208 cases passed (13 ms)
	// Your runtime beats 36.26 % of cpp submissions
	// Your memory usage beats 82.01 % of cpp submissions (14.7 MB)
    ListNode* mergeTwoLists(ListNode* list1, ListNode* list2) {
		if (!list1 && !list2) return (ListNode *) nullptr;
		if (!list1) return list2;
		if (!list2) return list1;
		ListNode * t1 = list1, *t2 = list2;
		ListNode * merged;
		if (t1 -> val > t2 -> val) {
			merged = t2;
			t2 = t2 -> next;
			merged -> next = nullptr;
		} else {
			merged = t1;
			t1 = t1 -> next;
			merged -> next = nullptr;
		}

		ListNode *mtemp = merged;
		while (t1 && t2) {
			if (t1 -> val > t2 -> val) {
				mtemp -> next = t2;
				t2 = t2 -> next;
				mtemp = mtemp -> next;
				mtemp -> next = nullptr;
			} else {
				mtemp -> next = t1;
				t1 = t1 -> next;
				mtemp = mtemp -> next;
				mtemp -> next = nullptr;
			}
		}
		if (!t1 && t2) mtemp -> next = t2;
		else if (!t2 && t1) mtemp -> next =t1;
		return merged;
    }
};
// @lc code=end

