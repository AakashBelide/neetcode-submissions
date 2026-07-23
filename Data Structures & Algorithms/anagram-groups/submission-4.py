class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        patterns = {}
        for word in strs:
            alpha = [0]*26
            for l in word:
                alpha[ord(l) - ord("a")] += 1
            if tuple(alpha) not in patterns:
                patterns[tuple(alpha)] = [word]
            else:
                patterns[tuple(alpha)].append(word)
        output = []

        for pattern in patterns:
            output.append(patterns[pattern])
        
        return output