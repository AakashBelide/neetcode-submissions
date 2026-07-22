class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if len(s)==0:
            return 0
        i = 0
        j = 1
        output = 1
        freq = set()
        freq.add(s[i])
        while i<j and j<len(s):
            if s[j] not in freq:
                freq.add(s[j])
            else:
                while s[j] in freq:
                    freq.remove(s[i])
                    i += 1
                freq.add(s[j])
            output = max(output, j-i+1)
            j += 1
        
        return output