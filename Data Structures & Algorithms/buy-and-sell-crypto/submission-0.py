class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        left = []
        right = [0]*len(prices)
        left_min = 99999999
        right_max = 0

        for i in range(len(prices)):
            left_min = min(left_min, prices[i])
            left.append(left_min)
        
        for i in range(len(prices)-1, -1, -1):
            right_max = max(right_max, prices[i])
            right[i] = right_max
        
        profit = 0

        for i in range(len(left)):
            profit = max(profit, right[i]-left[i])

        return profit