class Solution(object):
    def isIsomorphic(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        mapping = {}
        covered = set()
        if len(s) != len(t):
            return False
        for i in range(len(s)):
            if s[i] in mapping:
                if mapping[s[i]] != t[i]:
                    return False
            else:
                if t[i] in covered:
                    return False
                mapping[s[i]] = t[i]
                covered.add(t[i])
        return True
