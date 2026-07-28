class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s2)<len(s1):
            return False
        alpha1 = {}
        tot1 = 0
        for i in range(len(s1)):
            if s1[i] not in alpha1:
                alpha1[s1[i]] = 0
            alpha1[s1[i]] += 1
            tot1 += 1
        alpha2 = {}
        tot2 = 0
        for j in range(len(s1)):
            if s2[j] in alpha1:
                if s2[j] not in alpha2:
                    alpha2[s2[j]] = 0
                alpha2[s2[j]] += 1
                if alpha2[s2[j]]<=alpha1[s2[j]]:
                    tot2 += 1
        l = 0
        r = len(s1)
        while r<len(s2):
            if tot1 == tot2:
                return True
            
            if s2[r] in alpha1:
                if s2[r] not in alpha2:
                    alpha2[s2[r]] = 0
                alpha2[s2[r]] += 1
                if alpha2[s2[r]]<=alpha1[s2[r]]:
                    tot2 += 1

            if s2[l] in alpha1:
                if alpha2[s2[l]]<=alpha1[s2[l]]:
                    tot2 -= 1
                alpha2[s2[l]] -= 1
                
            l += 1
            r += 1
        if tot1 == tot2:
            return True
        return False
        
