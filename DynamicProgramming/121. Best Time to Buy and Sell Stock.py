"""
121. Best Time to Buy and Sell Stock
Easy

Say you have an array for which the ith element is the price of a given stock on day i.

If you were only permitted to complete at most one transaction (i.e., buy one and sell one share of the stock), 
design an algorithm to find the maximum profit.

Note that you cannot sell a stock before you buy one.

Example 1:

Input: [7,1,5,3,6,4]
Output: 5
Explanation: Buy on day 2 (price = 1) and sell on day 5 (price = 6), profit = 6-1 = 5.
             Not 7-1 = 6, as selling price needs to be larger than buying price.
Example 2:

Input: [7,6,4,3,1]
Output: 0
Explanation: In this case, no transaction is done, i.e. max profit = 0.
"""

class Solution:
    def maxProfit(self, prices):
        if not prices:
            return 0
        # 储存当天之前的最大值
        res = 0
        # profit[i][j] 第i天的最大利润 j为第i天及之前的总共交易次数0次，1买了一次，2买了又卖了
        profit = [[0 for _ in range(3)] for _ in range(len(prices))]
        # 边界值；第一天 不卖，买了，买了又卖了
        profit[0][0], profit[0][1], profit[0][2] = 0, -prices[0], 0
        for i in range(1, len(prices)):
            # 0表示该天还是不买
            profit[i][0] = profit[i-1][0]
            # 1表示该天之前或该天买了
            profit[i][1] = max(profit[i-1][1], profit[i-1][0]-prices[i])
            # 2表示该天之前已经一买一卖 或者该天卖了
            profit[i][2] = max(profit[i-1][2], profit[i-1][1]+prices[i])
            res = max(res, profit[i][0], profit[i][1],profit[i][2])
        return res
