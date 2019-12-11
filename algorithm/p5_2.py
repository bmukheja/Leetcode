class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        # Expand around centers, there are only 2n-1 centers
        if s == None or len(s)<1:
            return ""
        start = end = 0
        for i in range(len(s)):
            len1 = expandAroundCenter(s,i,i)
            len2 = expandAroundCenter(s,i,i+1)
            curlen = max(len1,len2)
            if curlen> (end-start):
                start = i - (curlen-1)/2
                end = i+ curlen/2
        return s[start:end+1]

def expandAroundCenter(s,left,right):
    while left >=0 and right < len(s) and s[left] == s[right]:
        left -=1
        right +=1
    return right - left + 1