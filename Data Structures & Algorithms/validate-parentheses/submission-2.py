class Solution:
    def isValid(self, s: str) -> bool:

        stack = []

        for p in s:

            if p == '{' or p == '[' or p == '(' :
                stack.append(p)
            elif len(stack) == 0:
                return False
            else:
                if p == '}' and stack[-1] == '{':
                    stack.pop()
                elif p == ')' and stack[-1] == '(':
                    stack.pop()
                elif p == ']' and stack[-1] == '[':
                    stack.pop()
                else:
                    return False

            print(stack)

        if len(stack) == 0:
            return True
        return False
        