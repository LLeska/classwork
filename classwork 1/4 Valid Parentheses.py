class Solution(object):
    def isValid(self, s):
        stack = []
        pairs = {
            ')': '(',
            ']': '[',
            '}': '{'
        }
        for c in s:
            if c in '([{':
                stack.append(c)
            else:
                if not stack:
                    return False
                if stack[-1] != pairs[c]:
                    return False
                stack.pop()
        return len(stack) == 0