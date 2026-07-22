class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        i = 1
        output = [0]*len(temperatures)
        stack = [0]
        while i<len(temperatures):
            while stack and temperatures[i]>temperatures[stack[-1]]:
                rem = stack.pop()
                output[rem] = i - rem
            stack.append(i)
            i += 1
        return output