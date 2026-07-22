class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        pos_speed = []

        for i in range(len(speed)):
            pos_speed.append([position[i], speed[i]])
        
        pos_speed.sort(reverse=True)

        # print(pos_speed)

        time_reach = []

        for i in range(len(pos_speed)):
            distance = target - pos_speed[i][0]
            time = distance/pos_speed[i][1]
            time_reach.append(time)
            if len(time_reach) >= 2 and time_reach[-1] <= time_reach[-2]:
                time_reach.pop()
        
        return len(time_reach)