class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        cur = {}
        pos = 0
        prevpos = 0
        maxlen = 0

        for pos in range(len(s)):
            if s[pos] in cur:
                prevpos = max(cur.get(s[pos]) + 1, prevpos)
            maxlen = max(maxlen, pos - prevpos + 1)
            cur[s[pos]] = pos

        return maxlen