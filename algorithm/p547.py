from typing import List
class Solution:
    def findCircleNum(self, M: List[List[int]]) -> int:
        N = len(M)
        n_circles = 0

        for i in range(N):
            for j in range(N):
                if M[i][j]==1:
                    n_circles+=1
                    self.dfs(M,i,j)
        return n_circles

    def dfs(self, M, i, j):
        M[i][j] = 0
        for k in range(len(M)):
            if M[k][j]==1:
                self.dfs(M,k,j)
        for k in range(len(M[0])):
            if M[i][k]==1:
                self.dfs(M,i,k)

print(Solution().findCircleNum([[1,0,0,1],[0,1,1,0],[0,1,1,1],[1,0,1,1]]))