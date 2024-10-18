from heapq import heappop, heappush
from collections import defaultdict
import math
class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        adj = defaultdict(list)
        for u, v, price in flights:
            adj[u].append((v, price))
            
        heap = [(0, src, k+1)]
        
        min_costs = [[math.inf] * (k + 2) for _ in range(n)]
        min_costs[src][k + 1] = 0
        
        while heap:
            cost, city, stops = heapq.heappop(heap)
            if city == dst:
                return cost
            if stops > 0:
                for nei, price in adj[city]:
                    newcost = cost + price
                    if newcost < min_costs[nei][stops - 1]:
                        min_costs[nei][stops - 1] = newcost
                        heappush(heap, (newcost, nei, stops - 1))
        
        return -1