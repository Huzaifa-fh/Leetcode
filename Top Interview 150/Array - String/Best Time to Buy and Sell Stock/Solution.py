class Solution:
    def maxProfit(self, prices: List[int]) -> int:

        left = 0
        right = 1
        n = len(prices)
        max_profit = 0

        while right < n:
            if prices[left] < prices[right]:
                curr_profit = prices[right] - prices[left]
                max_profit = max(curr_profit, max_profit)
            else:
                left = right

            right += 1

        return max_profit


