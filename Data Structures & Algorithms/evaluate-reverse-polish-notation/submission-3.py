class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []

        def operate(first, second, op):
            if op == "+":
                return first + second
            elif op == "-":
                return first - second
            elif op == "*":
                return first * second
            elif op == "/":
                return first / second
        
        ops = {"+",  "-", "/", "*"}

        for i in range(len(tokens)):
            if tokens[i] not in ops:
                stack.append(int(tokens[i]))
            else:
                top = stack.pop()
                bottom = stack.pop()
                stack.append(int(operate(bottom, top, tokens[i])))
        
        return int(stack[-1])