#
# @lc app=leetcode id=121 lang=python3
#
# [121] Best Time to Buy and Sell Stock
#
from typing import List
# @lc code=start
class maxProfit:
    def maxProfit(self, prices: List[int]) -> int:
        max_profit, min_price = 0, float('inf')

        for price in prices:
            min_price = min(min_price, price)
            profit = price - min_price
            max_profit = max(profit, max_profit)

        return max_profit

        # max_profit = 0
        # if len(prices) == 1:
        #     return 0
    
        # for i in range(len(prices) - 1):
        #     profit = max(prices[i+1:]) - prices[i]
        #     max_profit = max(max_profit, profit)

        # if max_profit > 0:
        #     return max_profit
        # else:
        #     return 0

        # desc_sort = sorted(prices, key=int, reverse=True)
        # if prices == desc_sort:
        #     return 0

        # max_profit = 0
        # if len(prices) == 1:
        #     return 0
        # elif len(prices) == 2:
        #     if (prices[1] - prices[0]) > 0:
        #         return (prices[1] - prices[0])
        #     else:
        #         return 0
        # elif len(prices) >= 3:
        #     for i in range(len(prices) - 1):
        #         for j in range(i+1, len(prices)):
        #             profit = prices[j] - prices[i]
        #             if profit > max_profit:
        #                 max_profit = profit
        
        # if max_profit > 0:
        #     return max_profit
        # else:
        #     return 0
# @lc code=end
if __name__ == "__main__":
    maxProfit = maxProfit()
    maxProfit.maxProfit([7, 1, 5, 3, 6, 4])
    maxProfit.maxProfit([2,1,4])