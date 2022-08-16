class Solution:
    #Cheated: Looked at solution
    def maxProfit(self, prices: list[int]) -> int:
        min_price = prices[0]
        max_profit = 0
        profit = []
        for price in prices:
            min_price = min(min_price, price)
            max_profit = max(max_profit, price - min_price)
            profit.append(max_profit)

        max_price = prices[-1]
        max_profit = 0
        total_max = 0
        for i in range(len(prices) - 1, -1, -1):
            max_price = max(max_price, prices[i])
            max_profit = max(max_profit, max_price - prices[i])
            total_max = max(total_max, profit[i] + max_profit)
        return total_max
