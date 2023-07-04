from collections import deque

class Solution:
    def isValid(self, s: str) -> bool:

        n = len(s)
        stack = deque()

        for i in range(n):
            if s[i] in ['(', '{', '[']:
                stack.append(s[i])
            elif len(stack) > 0:
                if s[i] == ')' and stack[-1] == '(':
                    stack.pop()
                elif s[i] == '}' and stack[-1] == '{':
                    stack.pop()
                elif s[i] == ']' and stack[-1] == '[':
                    stack.pop()
                else:
                    stack.append(s[i])
            else:
                stack.append(s[i])

        return len(stack) == 0
