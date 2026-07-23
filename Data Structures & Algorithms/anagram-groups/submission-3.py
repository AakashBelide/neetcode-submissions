class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        patterns = {}
        for word in strs:
            alpha = [0]*26
            for l in word:
                alpha[ord(l) - ord("a")] += 1
            pattern = ""
            for al in alpha:
                pattern += f" {str(al)}"
            if pattern not in patterns:
                patterns[pattern] = [word]
            else:
                patterns[pattern].append(word)
        output = []

        for pattern in patterns:
            output.append(patterns[pattern])
        
        return output