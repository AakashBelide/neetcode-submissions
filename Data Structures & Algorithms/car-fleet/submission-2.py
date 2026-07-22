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
        
        # print(time_reach)

        # fleets = 0

        # stack = []

        # for j in range(len(time_reach)):
        #     if not stack:
        #         stack.append(time_reach[j])
        #     else:
        #         if time_reach[j]>stack[-1]:
        #             fleets += 1
        #         stack.append(time_reach[j])
        
        # return fleets