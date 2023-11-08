class Solution:
    def maxProfit(self, prices: List[int]) -> int:
                # if prices is None or len(prices) == 0:
        if not prices:
            return 0
        # variable to store the minimum price
        min_price = prices[0]
        # variable to store the maximum profit
        max_profit = 0
        # iterate through the prices
        for i in range(1,len(prices)):
        # if the current price is less than the minimum price
            if prices[i] < min_price:
        # update the minimum price
                min_price = prices[i]
            else:
        # commpute the profit by subtracting the current price from the minimum price
                max_profit = max(max_profit, prices[i]-min_price)
        return max_profit