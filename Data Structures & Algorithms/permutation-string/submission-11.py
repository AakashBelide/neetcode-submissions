class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s2) < len(s1):
            return False
        
        s1_freq = [0]*26
        uni_count = 0
        
        for i in range(len(s1)):
            ind = ord(s1[i]) - ord('a')

            if s1_freq[ind] == 0:
                uni_count += 1
            
            s1_freq[ind] += 1
        
        left = 0
        right = 0
        s2_freq = [0]*26
        matches = 26 - uni_count
        
        while right < len(s2):
            if right>=len(s1):
                left_ind = ord(s2[left]) - ord('a')
                s2_freq[left_ind] -= 1
                if s2_freq[left_ind] == s1_freq[left_ind]:
                    matches += 1
                elif s2_freq[left_ind] == s1_freq[left_ind] - 1:
                    matches -= 1
                left += 1
            
            right_ind = ord(s2[right]) - ord('a')
            s2_freq[right_ind] += 1
            if s2_freq[right_ind] == s1_freq[right_ind]:
                matches += 1
            elif s2_freq[right_ind] == s1_freq[right_ind] + 1:
                matches -= 1
            right += 1

            if matches == 26:
                return True
        
        return False