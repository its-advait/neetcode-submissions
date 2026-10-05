import operator

class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        d = {
            "+": operator.add,
            "-": operator.sub,
            "*": operator.mul,
        }
        for token in tokens:
            if token == "/":
                right = stack.pop()
                left = stack.pop()
                stack.append(int(left/right))
            elif token in d:
                right = stack.pop()
                left = stack.pop()
                stack.append(d[token](left, right))
            else:
                stack.append(int(token))
        return stack[-1]
