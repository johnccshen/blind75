from typing import List


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        left = 0 # Buy
        right = 1 # Sell
        max_profit = 0
        while right < len(prices):
            profit = prices[right] - prices[left]
            if prices[right] > prices[left]:
                max_profit = max(max_profit, profit)
            else:
                left = right
            right += 1
        return max_profit
