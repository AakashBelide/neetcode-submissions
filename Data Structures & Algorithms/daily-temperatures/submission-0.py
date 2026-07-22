class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        i = 1
        output = [0]*len(temperatures)
        stack = [[temperatures[0], 0]]
        while i<len(temperatures):
            while stack and temperatures[i]>stack[-1][0]:
                rem = stack.pop()
                output[rem[1]] = i - rem[1]
            stack.append([temperatures[i], i])
            i += 1
        return output