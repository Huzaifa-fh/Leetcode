from collections import deque

class Solution:
    def isValid(self, s: str) -> bool:

        n = len(s)
        stack = deque()

        for i in range(n):
            if s[i] in ['(', '{', '[']:
                stack.append(s[i])
            else:
                if not stack:
                    return False

                if s[i] == ')' and stack[-1] == '(':
                    stack.pop()
                elif s[i] == '}' and stack[-1] == '{':
                    stack.pop()
                elif s[i] == ']' and stack[-1] == '[':
                    stack.pop()
                else:
                    return False

        return len(stack) == 0
