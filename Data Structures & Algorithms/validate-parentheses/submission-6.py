class Solution:
    def isValid(self, s: str) -> bool:
        open_map = {"{": "}", "[": "]", "(": ")"}
        close_map = { "}": "{", "]": "[", ")": "("}

        stack = []

        for op in s:
            # print(stack)
            if op in open_map:
                stack.append(op)
            else:
                if stack and stack[-1] == close_map[op]:
                    stack.pop()
                else:
                    return False
        
        if len(stack)!=0:
            return False
        
        return True
