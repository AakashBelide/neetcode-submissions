class Solution:
    def isValid(self, s: str) -> bool:
        checkOp = {"(": ")", "[": "]", "{": "}"}
        stack = []
        i = 0

        while i<len(s):
            if s[i] in checkOp:
                stack.append(s[i])
            else:
                if ((len(stack)<1) or (checkOp[stack.pop()] != s[i])):
                    return False
            i += 1
        
        if len(stack)!=0:
            return False

        return True