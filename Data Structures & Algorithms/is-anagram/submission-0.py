class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        alpha = [0]*26

        for i in s:
            alpha[ord(i) - ord("a")] += 1
        
        for j in t:
            alpha[ord(j) - ord("a")] -= 1
        
        for k in alpha:
            if k!= 0:
                return False 
        return True
        