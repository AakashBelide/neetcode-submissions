class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        patterns = defaultdict(list)
        for word in strs:
            alpha = [0]*26
            for l in word:
                alpha[ord(l) - ord("a")] += 1
            patterns[tuple(alpha)].append(word)
        output = []

        for pattern in patterns:
            output.append(patterns[pattern])
        
        return output