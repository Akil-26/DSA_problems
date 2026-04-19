class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        for val in tokens:
            if val == '+':
                stack.append(stack.pop() + stack.pop())
            elif val == '-':
                b, a = stack.pop(),stack.pop()
                stack.append(a-b)
            elif val == '*':
                stack.append(stack.pop() * stack.pop())
            elif val == '/':
                b, a = stack.pop(),stack.pop()
                stack.append(int(float(a) / b))
            else:
                stack.append(int(val))
        return stack[0]