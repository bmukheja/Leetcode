from typing import List
from pprint import pprint

class Solution:
    def pacificAtlantic(self, matrix: List[List[int]]) -> List[List[int]]:
        self.y_max = len(matrix)
        self.x_max = len(matrix[0])
        self.pacific = [[False for x in range(self.x_max)] for y in range(self.y_max)]
        self.atlantic = [[False for x in range(self.x_max)] for y in range(self.y_max)]

        #Top row and last row
        for x in range(self.x_max):
            self.pacific[0][x] = True
            self.atlantic[-1][x] = True

        #Left column and right column
        for y in range((self.y_max)):
            self.pacific[y][0] = True
            self.atlantic[y][-1] = True

        self.visited = set()
        output = []
        for y in range(self.y_max):
            for x in range(self.x_max):
                self.dfs(x,y,matrix)
                if self.pacific[y][x] and self.atlantic[y][x]:
                    output.append((y,x))
        return output


    def dfs(self,x,y,matrix):

        if (x,y) in self.visited:
            return
        self.visited.add((x,y))
        for x1,y1 in [(x+1,y),(x-1,y),(x,y+1),(x,y-1)]:
            if self.atlantic[y][x] and self.pacific[y][x]:
                break
            if x1 < 0 or x1 > self.x_max - 1 or y1 < 0 or y1 > self.y_max - 1:
                continue
            if matrix[y1][x1] < matrix[y][x]:
                if x==3 and y==1:
                    print("here")
                self.dfs(x1,y1,matrix)
                if self.pacific[y1][x1]:
                    self.pacific[y][x] = True
                if self.atlantic[y1][x1]:
                    self.atlantic[y][x] = True


print(Solution().pacificAtlantic(
[
[1,2,2,3,5],
[3,2,3,4,4],
[2,4,5,3,1],
[6,7,1,4,5],
[5,1,1,2,4]
]))