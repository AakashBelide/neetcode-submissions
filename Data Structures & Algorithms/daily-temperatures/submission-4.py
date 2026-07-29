class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        n = len(temperatures)
        output = [0]*n
        for i in range(n-2, -1, -1):
            j = i + 1
            while j < n and temperatures[j] <= temperatures[i]:
                if output[j]==0:
                    j = n
                    break
                j+= output[j]
            
            if j<n:
                output[i] = j - i
        return output