class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit = 0
        r_max = prices[-1]
        for i in range(len(prices)-2, -1, -1):
            profit = max(profit, r_max - prices[i])
            r_max = max(r_max, prices[i])
        return profit