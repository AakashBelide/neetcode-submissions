class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        alpha = {}
        l = 0
        output = 0

        for r in range(len(s)):
            if s[r] in alpha:
                l = max(alpha[s[r]]+1, l)
            alpha[s[r]] = r
            output = max(output, r-l+1)
        return output