#
# @lc app=leetcode id=121 lang=python3
#
# [121] Best Time to Buy and Sell Stock
#

# @lc code=start
class Solution:
	def maxProfit(self, prices: List[int]) -> int:
		profit = 0
		min = prices[0]

		for price in prices:
			lcl_profit = price - min
			if lcl_profit > profit:
				profit = lcl_profit
			if price < min:
				min = price

		return profit 

# @lc code=end
