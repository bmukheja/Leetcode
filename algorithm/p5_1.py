class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        #Use a DP 2D array with the brute force method of checking every substring
        n = len(s)
        P = [[None] * n for i in range(n)]
        maxlen = 0
        maxstr = ""
        for col in range(n):
            for row in range(col + 1):
                if row == col:
                    P[row][col] = True
                elif row + 1 == col:
                    P[row][col] = s[row] == s[col]
                else:
                    P[row][col] = P[row + 1][col - 1] and s[row] == s[col]

                if P[row][col] == True and (col - row + 1) > maxlen:
                    maxlen = col - row + 1
                    maxstr = s[row:col + 1]
        return maxstr
