from typing import List


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)

        prefix_profit = [0]*(n)
        prefix_profit[0] = 0
        prefix_min = prices[0]
        for i in range(1, n):
            prefix_min = min(prices[i], prefix_min)
            new_profit = prices[i] - prefix_min
            prefix_profit[i] = max(prefix_profit[i-1], new_profit)

        suffix_profit = 0
        suffix_max = prices[n-1]
        profit = suffix_profit
        for i in range(n-2, -1, -1):
            suffix_max = max(prices[i], suffix_max)
            new_profit = suffix_max - prices[i]
            suffix_profit = max(suffix_profit, new_profit)
            profit_n = prefix_profit[i] + suffix_profit
            profit = max(profit, profit_n)

        return profit
