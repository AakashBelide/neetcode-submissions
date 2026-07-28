class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        l = 0
        mx_q = deque()
        output = []

        for r in range(len(nums)):
            while mx_q and mx_q[-1]<nums[r]:
                mx_q.pop()
            
            mx_q.append(nums[r])
            mx = mx_q[0]

            if r-l+1 == k:
                output.append(mx)

                if nums[l] == mx:
                    mx_q.popleft()
                l += 1
        
        return output