class Solution:
    def maxProfit(self, prices: List[int]) -> int:

        total_profit = 0
        n = len(prices)

        for i in range(1, n):
            if prices[i] > prices[i - 1]:
                total_profit += prices[i] - prices[i - 1]

        return total_profit
