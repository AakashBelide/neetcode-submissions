class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if len(t)>len(s):
            return ""
        alpha_t, alpha_s, tot_t, tot_s = defaultdict(int), defaultdict(int), len(t), 0
        for i in range(len(t)):
            alpha_t[t[i]] += 1
        l = 0
        output = s
        out_bool = False
        for r in range(len(s)):
            # print("Out", s[l:r+1], l ,r)
            if s[r] in alpha_t:
                alpha_s[s[r]] += 1
                if alpha_s[s[r]] <= alpha_t[s[r]]:
                    tot_s += 1
            if tot_s >= tot_t:
                # if len(s[l:r+1])<len(output):
                #     output = s[l:r+1]
                while tot_s >= tot_t:
                    # print("In", s[l:r+1], l, r)
                    if s[l] in alpha_s:
                        alpha_s[s[l]] -= 1
                        if alpha_s[s[l]] < alpha_t[s[l]]:
                            tot_s -= 1
                    if len(s[l:r+1])<=len(output):
                        output = s[l:r+1]
                        out_bool = True
                    l += 1
        if out_bool:
            return output
        else:
            return ""