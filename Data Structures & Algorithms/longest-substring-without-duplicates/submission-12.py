class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if len(s)<1:
            return 0
        alpha_count = {}
        i = 0
        j = 1
        alpha_count[s[i]] = i
        output = 1
        out_text = ""
        while j<len(s):
            if s[j] not in alpha_count:
                alpha_count[s[j]] = j
                print("A", i, j, s[i:j])
            else:
                for k in range(i, alpha_count[s[j]]):
                    del alpha_count[s[k]]
                i = alpha_count[s[j]]+1
                alpha_count[s[j]] = j
                print("B", i, j, s[i:j])
            j += 1
            print("C", i, j, s[i:j])
            if (j-i)>output:
                output = j-i
                out_text = s[i:j]
        print(out_text)
        return output