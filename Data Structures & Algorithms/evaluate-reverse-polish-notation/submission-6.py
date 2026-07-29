class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        ops = {"+", "-", "/", "*"}
        for token in tokens:
            if token not in ops:
                stack.append(int(token))
            else:
                b = stack.pop()
                a = stack.pop()
                if token == "+":
                    c = a + b
                elif token == "-":
                    c = a - b
                elif token == "*":
                    c = a * b
                elif token == "/":
                    c = a/b
                stack.append(int(c))
        return stack[-1]