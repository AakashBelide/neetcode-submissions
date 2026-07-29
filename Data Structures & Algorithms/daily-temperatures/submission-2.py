class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack = []
        output = [0]*len(temperatures)
        for i in range(len(temperatures)):
            # print(stack, i)
            while stack and stack[-1][0]<temperatures[i]:
                tmp = stack.pop()
                output[tmp[1]] = i - tmp[1]
            stack.append([temperatures[i], i])
            # print(stack)
        return output