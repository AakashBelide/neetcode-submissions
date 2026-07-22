class Solution:
    def minWindow(self, s: str, t: str) -> str:
        output = ""
        output_size = 9999999999
        
        if len(t)>len(s):
            return output
        
        t_freq, s_freq = {}, {}
        
        uni_count = 0

        for i in range(len(t)):
            if t[i] not in t_freq:
                t_freq[t[i]] = 1
            else:
                t_freq[t[i]] += 1
        
        have, need = 0, len(t_freq)
        l = 0
        
        for r in range(len(s)):
            c = s[r]
            if c not in s_freq:
                s_freq[c] = 1
            else:
                s_freq[c] += 1
        
            if c in t_freq and s_freq[c] == t_freq[c]:
                have += 1
            
            while have == need:
                if (r - l + 1) < output_size:
                    output_size = r - l + 1
                    output = s[l:r+1]
                
                c2 = s[l]
                s_freq[c2] -= 1

                if c2 in t_freq and s_freq[c2] < t_freq[c2]:
                    have -= 1 
                l += 1
        
        return output