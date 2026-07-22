import math
class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        left = 1
        right = max(piles)
        res = right

        while left<=right:
            mid = (right + left)//2
            
            time_taken = 0
            for pile in piles:
                time_taken += math.ceil(pile/mid)
            
            if h < time_taken:
                left = mid + 1
            elif h >= time_taken:
                res = mid
                right = mid - 1
        
        return res