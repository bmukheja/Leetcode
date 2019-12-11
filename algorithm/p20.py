class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        match = {'{':'}','(':')','[':']'}
        for char in s:
            if char in ['{','(','[']:
                stack.append(char)
            else:
                if not stack:
                    return False
                else:
                    temp = stack.pop(-1)
                    if char != match.get(temp):
                        return False
        if stack:
            return False
        return True
