class Solution:

    def encode(self, strs: List[str]) -> str:
        encode_strs = ""
        for i in range(len(strs)):
            encode_str = ""
            if strs[i] == "":
                encode_str += "e"
            else:
                for j in range(len(strs[i])):
                    encode_str += str(ord(strs[i][j]))
                    if j != len(strs[i])-1:
                        encode_str += ", "
            encode_strs += encode_str
            if i != len(strs)-1:
                encode_strs += " | "
        return encode_strs
    
    def decode(self, s: str) -> List[str]:
        if s == "":
            return []
        encoded_list = s.split(" | ")
        decoded_list = []
        for encoded_str in encoded_list:
            decode_list = encoded_str.split(", ")
            decode_str = ""
            for ords in decode_list:
                if ords == "e":
                    decode_str += ""
                else:
                    decode_str += chr(int(ords))
                  
            decoded_list.append(decode_str)
        
        return decoded_list