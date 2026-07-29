class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack = []
        n = len(temperatures)
        output = [0]*n
        for i in range(n):
            while stack and stack[-1][0]<temperatures[i]:
                tmp = stack.pop()
                output[tmp[1]] = i - tmp[1]
            stack.append([temperatures[i], i])
        return output