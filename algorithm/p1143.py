

class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        """
        DP solution. Create a 2-d dp array.
        Bottom-up DP utilizes a matrix m where we track LCS sizes for each combination of i and j.

        If a[i] == b[j], LCS for i and j would be 1 plus LCS till the i-1 and j-1 indexes.
        Otherwise, we will take the largest LCS if we skip a charracter from one of the string (max(m[i - 1][j], m[i][j - 1]).
        """
        dp = [[0]*(len(text2)+1) for _ in range(len(text1)+1)]
        for i in range(1,len(text1)+1):
            for j in range(1,len(text2)+1):
                if text1[i-1] == text2[j-1]:
                    dp[i][j] = dp[i-1][j-1]+1
                else:
                    dp[i][j] = max(dp[i-1][j],dp[i][j-1])
        return dp[len(text1)][len(text2)]


print(Solution().longestCommonSubsequence(text1 = "abcde", text2 = "ace"))
print(Solution().longestCommonSubsequence(text1 = "abc", text2 = "abc"))
print(Solution().longestCommonSubsequence( text1 = "abc", text2 = "def"))

