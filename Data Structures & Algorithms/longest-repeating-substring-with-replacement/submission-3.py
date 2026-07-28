class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        alpha = defaultdict(int)
        max_f = 0
        l = 0
        output = 0
        for r in range(len(s)):
            alpha[s[r]] += 1
            max_f = max(max_f, alpha[s[r]])

            while (r-l+1) - max_f > k:
                alpha[s[l]] -= 1
                l += 1
            output = max(output, r-l+1)
        
        return output