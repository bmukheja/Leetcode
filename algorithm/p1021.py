class Solution(object):
    def removeOuterParentheses(self, S):
        """
        :type S: str
        :rtype: str
        """
        stack = []
        output = []
        current = []

        for char in S:
            if not stack:
                stack.append(char)
                continue
            if len(stack) == 1 and char == ')':
                output.append(''.join(current))
                current = []
                stack.pop(-1)
                continue
            if char == ')':
                current.append(char)
                stack.pop(-1)
            else:
                stack.append(char)
                current.append(char)
        return ''.join(output)