class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if len(s)<1:
            return 0
        alpha_count = {}
        i = 0
        j = 1
        alpha_count[s[i]] = i
        output = 1

        while j<len(s):
            if s[j] not in alpha_count:
                alpha_count[s[j]] = j
            else:
                for k in range(i, alpha_count[s[j]]):
                    del alpha_count[s[k]]
                i = alpha_count[s[j]]+1
                alpha_count[s[j]] = j
            
            j += 1
            
            if (j-i)>output:
                output = j-i
                out_text = s[i:j]
        
        return output