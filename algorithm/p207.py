from typing import List

class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        # Graph cycle detection
        # First represent the graph as adjacency dict
        self.adjacent = {}
        for edge in prerequisites:
            child,parent = edge
            if not self.adjacent.get(parent):
                self.adjacent[parent] = []
            self.adjacent[parent].append(child)

        self.visited = set()
        self.visiting = set()
        for course in range(numCourses):
            if not self.dfs(course):
                return False
        return True


    def dfs(self, curnode):
        if curnode in self.visited:
            return True
        if curnode in self.visiting:
            return False
        self.visiting.add(curnode)
        for child in self.adjacent.get(curnode,[]):
            if not self.dfs(child):
                return False
        self.visiting.remove(curnode)
        self.visited.add(curnode)

        return True


