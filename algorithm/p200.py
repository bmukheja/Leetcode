from typing import List

class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        # Traverse through the grid
        # When you find an island, do a dfs to neighboring vertices to mark them off
        # Increase the count by 1
        self.grid = grid
        count = 0
        for y in range(len(grid)):
            for x in range(len(grid[0])):
                if self.grid[y][x]==1:
                    count+=1
                    self.dfs(x,y)
        return count

    def dfs(self,x,y):
        if self.grid[y][x] == 0:
            return
        self.grid[y][x] = 0
        for x1,y1 in [(x+1,y),(x-1,y),(x,y+1),(x,y-1)]:
            if x1<0 or y1<0 or x1>=len(self.grid[0]) or y1>=len(self.grid):
                continue
            self.dfs(x1,y1)

print(Solution().numIslands([
    [1,1,1,1,0],
    [1,1,0,1,0],
    [1,1,0,0,0],
    [0,0,0,0,0]
]))

print(Solution().numIslands([
    [1,1,0,0,0],
    [1,1,0,0,0],
    [0,0,1,0,0],
    [0,0,0,1,1]
]))
