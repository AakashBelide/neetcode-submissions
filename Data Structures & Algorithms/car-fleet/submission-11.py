class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        common = [[position[i], speed[i]] for i in range(len(position))]
        common.sort(reverse = True)

        fleets = 1
        prev_time = (target-common[0][0])/common[0][1]
        for i in range(1, len(position)):
            curr_time = (target-common[i][0])/common[i][1]
            # print(i, prev_time, curr_time, common[i][0], common[i][1])
            if curr_time > prev_time:
                fleets += 1
                prev_time = curr_time
        return fleets