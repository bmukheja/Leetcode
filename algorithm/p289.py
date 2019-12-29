from typing import List


class Solution:
    def gameOfLife(self, board: List[List[int]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        # logic -> s = sum(nbrs(i)). if board[i]==0 and s==3: board2[i]=1
        #           elif board[i]==1: if s<2 or s>3:board2[i]=0
        # For in-place solution use dummy values for cells

        m = len(board)
        n = len(board[0])

        for x in range(n):
            for y in range(m):
                sum_nbrs = self.sumNeighbors(x, y, board, m, n)
                if board[y][x] == 0:
                    # If it comes to life
                    if sum_nbrs == 3:
                        board[y][x] = -1

                if board[y][x] == 1:
                    #If it lives
                    if (sum_nbrs == 2 or sum_nbrs == 3):
                        board[y][x] = 1
                    else:
                        board[y][x] = 2

        for x in range(n):
            for y in range(m):
                if board[y][x]==2:
                    board[y][x]=0
                elif board[y][x]==-1:
                    board[y][x]=1

        return board

    def sumNeighbors(self, x, y, board, m, n):
        s = 0
        for x1, y1 in [(x + 1, y), (x - 1, y), (x, y + 1), (x, y - 1), (x + 1, y + 1), (x - 1, y + 1), (x + 1, y - 1),
                       (x - 1, y - 1)]:
            if x1 < 0 or x1 >= n or y1 < 0 or y1 >= m:
                continue
            s += 1 if board[y1][x1]>0 else 0
        return s


print(Solution().gameOfLife([
  [0,1,0],
  [0,0,1],
  [1,1,1],
  [0,0,0]
]))