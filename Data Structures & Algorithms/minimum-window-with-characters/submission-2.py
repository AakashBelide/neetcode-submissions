class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if len(t)>len(s):
            return ""
        
        t_freq = [0]*(ord('z') + 1 - ord('A'))
        # print(ord('z') - ord('A'))

        # print(len(t_freq))
        
        uni_count = 0

        for i in range(len(t)):
            ind = ord(t[i]) - ord('A')
            # print(t[i], ind)
            if t_freq[ind] == 0:
                uni_count += 1
            t_freq[ind] += 1
        
        output = ""
        output_size = 9999999999

        for i in range(len(s)):
            tmp_s_freq = [0]*(ord('z') + 1 - ord('A'))
            left_ind = ord(s[i]) - ord('A')

            tmp_s_uni = 0

            if t_freq[left_ind]!=0:
                tmp_s_freq[left_ind] += 1
                visit = set()
                if tmp_s_freq[left_ind] >= t_freq[left_ind] and t_freq[left_ind] != 0 and s[i] not in visit:
                    tmp_s_uni += 1
                    visit.add(s[i])
                if tmp_s_uni == uni_count:
                    output_size = 1
                    output = s[i]
                j = i + 1
                while j < len(s):
                    right_ind = ord(s[j]) - ord('A')
                    tmp_s_freq[right_ind] += 1
                    if tmp_s_freq[right_ind] >= t_freq[right_ind] and t_freq[right_ind]!= 0 and s[j] not in visit:
                        tmp_s_uni += 1
                        visit.add(s[j])
                    if tmp_s_uni == uni_count:
                        if j - i < output_size:
                            output_size = j - i
                            output = s[i:j+1]
                    j += 1
        
        return output