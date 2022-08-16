class Solution:
    def maxProfit(self, prices: list[int]) -> int:
        result = 0
        for i in range(len(prices) - 1):
            if prices[i] < prices[i+1]:
                result += prices[i+1] - prices[i]
        return result
