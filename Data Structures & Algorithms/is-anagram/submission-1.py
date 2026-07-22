class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        alpha = [0]*26

        for i in s:
            diff = ord(i) - ord('a')
            alpha[diff] += 1
        
        for i in t:
            diff = ord(i) - ord('a')
            if alpha[diff] == 0:
                return False
            alpha[diff] -= 1
        
        return sum(alpha)==0