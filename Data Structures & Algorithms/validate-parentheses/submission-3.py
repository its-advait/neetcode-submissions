class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        c = {"{":"}", "[":"]", "(":")"}
        for char in s:
            if char in c:
                stack.append(char)
            else:
                if not stack:
                    return False
                if c[stack.pop()] != char:
                    return False
        return not stack