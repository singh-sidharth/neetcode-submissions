class Solution:
    def isValid(self, s: str) -> bool:
        if len(s) == 1:
            return False
        stack = []

        for c in s:
            if stack:
                if c == ')' and stack[-1] == '(':
                    stack.pop()
                    continue
                elif c == ']' and stack[-1] == '[':
                    stack.pop()
                    continue
                elif c == '}' and stack[-1] == '{':
                    stack.pop()
                    continue
            stack.append(c)
        return len(stack) == 0
