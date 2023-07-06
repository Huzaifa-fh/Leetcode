class Solution:
    def maxProfit(self, prices: List[int]) -> int:

        left = 0
        total_profit = 0
        n = len(prices)

        for right in range(n - 1):
            local_min = prices[right]
            local_max = prices[right + 1]
            check = False

            while local_min < local_max:
                right += 1
                local_min = local_max
                local_max = prices[right]
                check = True

            total_profit += prices[right] - prices[left]
            left = right if check else right + 1

        return total_profit

