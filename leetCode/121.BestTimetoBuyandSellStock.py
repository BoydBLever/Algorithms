# https://leetcode.com/problems/best-time-to-buy-and-sell-stock/
from typing import List

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # Step 1: Initialize min_price to a very large value and max_profit to 0
        min_price, max_profit = float('inf'), 0
        
        # Step 2: Loop through the prices
        for price in prices:
            # If current price is less than min_price, update min_price
            if price < min_price:
                min_price = price
            # Otherwise, calculate the profit and update max_profit if needed
            else:
                profit = price - min_price
                max_profit = max(max_profit, profit)
        
        # Step 3: Return max_profit
        return max_profit
    
#Neetcode solution
# Use L pointer to buy, R pointer to sell
# class Solution:
#     def maxProfit(self, prices: List[int]) -> int:
#         l, r = 0, 1 #left = buy, right = sell
#         maxP = 0

#         while r < len(prices):
#             #profitable ?
#             if prices[l] < prices[r]:
#                 profit = prices[r] - prices[l]
#                 maxP = max(maxP, profit)
#             else:
#                 l = r
#             r += 1
#         return maxP