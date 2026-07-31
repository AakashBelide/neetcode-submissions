import math
class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        if len(piles) == 1:
            return math.ceil(piles[0]/h)
        tot = 0
        max_speed = 0

        for pile in piles:
            tot += pile
            max_speed = max(max_speed, pile)
        min_speed = tot//h
        
        mid = (min_speed + max_speed)//2
        output = max_speed
        while min_speed <= max_speed:
            time = 0
            
            for pile in piles:
                time += math.ceil(pile/mid)
            
            if time <= h:
                output = min(output, mid)
                max_speed = mid-1
            else:
                min_speed = mid+1
            mid = (min_speed + max_speed)//2
        return output