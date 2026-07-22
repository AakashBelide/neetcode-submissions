class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s2) < len(s1):
            return False
        
        s1_freq, s2_freq = [0]*26, [0]*26
        
        for i in range(len(s1)):
            s1_freq[ord(s1[i]) - ord('a')] += 1
            s2_freq[ord(s2[i]) - ord('a')] += 1
        
        matches = 0
        for i in range(26):
            matches += 1 if s1_freq[i]==s2_freq[i] else 0
        
        left = 0
        
        for right in range(len(s1), len(s2)):
            if matches == 26:
                return True
            
            index = ord(s2[right]) - ord('a')
            s2_freq[index] += 1
            if s2_freq[index] == s1_freq[index]:
                matches += 1
            elif s2_freq[index] == s1_freq[index] + 1 :
                matches -= 1
            
            index = ord(s2[left]) - ord('a')
            s2_freq[index] -= 1
            if s2_freq[index] == s1_freq[index]:
                matches += 1
            elif s2_freq[index] == s1_freq[index] - 1:
                matches -= 1
            left += 1
        
        return matches == 26