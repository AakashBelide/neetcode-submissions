import math
class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        p_size = len(piles)
        right = 0
        for i in range(p_size):
            right = max(right, piles[i])
        
        left = 1
        output = right

        def checkSpeed(s):
            time_taken = 0
            for pile in piles:
                time_taken += math.ceil(pile/s)
            return time_taken

        while left<=right:
            mid = left + (right - left)//2
            time_taken= checkSpeed(mid)
            if h < time_taken:
                left = mid + 1
            elif h >= time_taken:
                output = mid
                right = mid - 1
        
        return output