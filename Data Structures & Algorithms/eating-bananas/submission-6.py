import math
class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        min_speed, max_speed = 1, max(piles)
        mid = (min_speed + max_speed)//2
        output = max_speed
        
        while min_speed <= max_speed:
            time = 0
            
            for pile in piles:
                time += math.ceil(pile/mid)
            
            if time <= h:
                output = mid
                max_speed = mid - 1
            else:
                min_speed = mid + 1
            
            mid = (min_speed + max_speed)//2
        
        return output