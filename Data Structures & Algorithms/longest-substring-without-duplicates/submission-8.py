class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l = 0
        r = 0
        output = 0
        freq = {}
        while r<len(s):
            if s[r] in freq:
                l = max(freq[s[r]] + 1, l)
            freq[s[r]] = r
            output = max(output, r-l+1)
            r += 1
        
        return output