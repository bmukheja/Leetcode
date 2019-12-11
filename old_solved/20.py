class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        if len(s)%2!=0:
            return False
        #Otherwise
        stack = []
        complement = {'(':')','{':'}','[':']'}
        for i in range(len(s)):
            if s[i] in ('(','{','['):
                stack.append(s[i])
            elif s[i] in (')','}',']'):
                if len(s):
                    temp = stack.pop()
                else:
                    return False
                if complement[temp]!=s[i]:
                    return False
            else:
                return False
        if len(stack)==0:
            return True
        else:
            return False
sol = Solution()
print(sol.isValid('(['))