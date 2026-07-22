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
        
        ops = set()
        ops.add("+")
        ops.add("-")
        ops.add("/")
        ops.add("*")

        for i in range(len(tokens)):
            # print("1", stack, tokens[i])
            if tokens[i] not in ops:
                stack.append(int(tokens[i]))
            else:
                # print("2", stack, tokens[i])
                top = stack.pop()
                bottom = stack.pop()
                stack.append(int(operate(bottom, top, tokens[i])))
        
        return int(stack[-1])