import math
class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        left = 1
        right = max(piles)
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