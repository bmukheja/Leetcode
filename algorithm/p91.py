class Solution:
    def numDecodings(self, s: str) -> int:
        """
        Start from the end. Each string can be decoded one way except where the start is <26
        """
        if s == "":
            return 0
        dp = [0]*(len(s)+1)
        dp[-1] = 1
        for i in range(len(s)-1,-1,-1):
            if s[i] != "0":
                dp[i] += dp[i+1]
            if i<(len(s)-1) and "09"<s[i:i+2]<"27":
                dp[i] += dp[i+2]
        return dp[0]




print(Solution().numDecodings("12"),2)
print(Solution().numDecodings("226"),3)
print(Solution().numDecodings("0"),0)