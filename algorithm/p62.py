class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        #Create a dp array of m+1,n+1 size
        # each element (j,k) can be reached in x+y ways where x is the value of (j-1,k)
        # and y is the value of (j,k-1)
        dp = [[0]*(m+1) for _ in range(n+1)]
        dp[1][1] = 1
        for j in range(1,n+1):
            for k in range(1,m+1):
                if j==1 and k==1:
                    continue
                dp[j][k] = dp[j-1][k] + dp[j][k-1]
        return dp[n][m]



print(Solution().uniquePaths(m=3,n=2),3)
print(Solution().uniquePaths(m=7,n=3),28)
print(Solution().uniquePaths(m=23,n=12),28)