from collections import deque
from typing import List
import sys

class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, K: int) -> int:
        visited = dict()
        queue = deque()
        queue.append((src,0,0)) #destination, total price, stop count
        stops = dict()
        for flight in flights:
            s = flight[0]
            d = flight[1]
            p = flight[2]
            if s not in stops:
                stops[s] = list()
            stops[s].append((d,p))

        min_price = sys.maxsize
        dest_found = False
        while queue:
            current, total_price, stop_count = queue.popleft()
            if current in visited and visited[current]<total_price:
                continue
            if stop_count > K+1:
                continue
            if current == dst:
                dest_found = True
                if total_price < min_price:
                    min_price = total_price
            visited[current] = total_price
            for next_stop,price in stops.get(current,[]):
                queue.append((next_stop, price+total_price, stop_count+1))

        if min_price==sys.maxsize or not dest_found:
            return -1
        return min_price

print(Solution().findCheapestPrice(15,[[10,14,43],[1,12,62],[4,2,62],[14,10,49],[9,5,29],[13,7,53],[4,12,90],[14,9,38],[11,2,64],[2,13,92],[11,5,42],[10,1,89],[14,0,32],[9,4,81],[3,6,97],[7,13,35],[11,9,63],[5,7,82],[13,6,57],[4,5,100],[2,9,34],[11,13,1],[14,8,1],[12,10,42],[2,4,41],[0,6,55],[5,12,1],[13,3,67],[3,13,36],[3,12,73],[7,5,72],[5,6,100],[7,6,52],[4,7,43],[6,3,67],[3,1,66],[8,12,30],[8,3,42],[9,3,57],[12,6,31],[2,7,10],[14,4,91],[2,3,29],[8,9,29],[2,11,65],[3,8,49],[6,14,22],[4,6,38],[13,0,78],[1,10,97],[8,14,40],[7,9,3],[14,6,4],[4,8,75],[1,6,56]],1,4,10))