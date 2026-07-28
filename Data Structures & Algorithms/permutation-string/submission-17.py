class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1)>len(s2):
            return False
        alpha1, alpha2, tot1, tot2 = defaultdict(int), defaultdict(int), len(s1), 0

        for i in range(tot1):
            alpha1[s1[i]] += 1
        
        for i in range(tot1):
            if s2[i] in alpha1:
                alpha2[s2[i]] += 1
                if alpha2[s2[i]] <= alpha1[s2[i]]:
                    tot2 += 1
        
        l, r = 0, len(s1)

        while r<len(s2):
            if tot1==tot2:
                return True
            
            if s2[r] in alpha1:
                alpha2[s2[r]] += 1
                if alpha2[s2[r]] <= alpha1[s2[r]]:
                    tot2 += 1
            if s2[l] in alpha1:
                if alpha2[s2[l]] <= alpha1[s2[l]]:
                    tot2 -= 1
                alpha2[s2[l]] -= 1
            
            l += 1
            r += 1
        
        if tot1==tot2:
                return True
        
        return False
