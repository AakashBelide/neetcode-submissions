class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        groups = {}
        for st in strs:
            tmp_alpha = [0]*26
            for j in range(len(st)):
                tmp_alpha[ord(st[j]) - ord("a")] += 1
            # print(tmp_alpha)
            group = ""
            for alpha in tmp_alpha:
                group += str(alpha) + ","
            if group not in groups:
                groups[group] = [st]
            else:
                groups[group].append(st)
        # print(groups)
        
        output = []
        
        for k in groups:
            output.append(groups[k])
        
        return output