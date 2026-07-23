class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        patterns = {}
        output = []
        for word in strs:
            alpha = [0]*26
            for l in word:
                alpha[ord(l) - ord("a")] += 1
            
            if tuple(alpha) not in patterns:
                patterns[tuple(alpha)] = len(output)
                output.append([word])
            else:
                output[patterns[tuple(alpha)]].append(word)
        
        return output