class Solution:
    def isValid(self, s: str) -> bool:
        def checkOp(left, right):
            if left == "(" and right == ")":
                return True
            elif left == "{" and right == "}":
                return True
            elif left == "[" and right == "]":
                return True
            else:
                False
        
        stack = []
        i = 0

        while i<len(s):
            if s[i] == "(" or s[i] == "[" or s[i] == "{":
                stack.append(s[i])
            else:
                if len(stack)<1:
                    return False
                top = stack.pop()
                if not checkOp(top, s[i]):
                    return False
            i += 1
        
        if len(stack)!=0:
            return False

        return True
            