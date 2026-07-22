class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s2) < len(s1):
            return False
        s1_freq = [0]*26
        for i in range(len(s1)):
            s1_freq[ord(s1[i]) - ord('a')] += 1
        
        right = 0
        s2_freq = [0]*26

        while right < len(s1):
            print(right, s1_freq, s2_freq)
            s2_freq[ord(s2[right]) - ord('a')] += 1
            if s1_freq == s2_freq:
                return True
            right += 1
        left = 0
        while right < len(s2):
            print(left, right, s1_freq, s2_freq)
            s2_freq[ord(s2[right]) - ord('a')] += 1
            s2_freq[ord(s2[left]) - ord('a')] -= 1
            if s1_freq == s2_freq:
                return True
            left += 1
            right += 1
        if s1_freq == s2_freq:
            return True
        return False