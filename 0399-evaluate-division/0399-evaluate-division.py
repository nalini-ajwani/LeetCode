from collections import defaultdict

class Solution(object):
    def calcEquation(self, equations, values, queries):
        """
        :type equations: List[List[str]]
        :type values: List[float]
        :type queries: List[List[str]]
        :rtype: List[float]
        """
        # Step 1: Build the graph
        graph = defaultdict(dict)
        for (A, B), value in zip(equations, values):
            graph[A][B] = value
            graph[B][A] = 1 / value
        
        # Step 2: DFS to find the result of each query
        def dfs(src, dst, visited):
            if src not in graph or dst not in graph:
                return -1.0
            if src == dst:
                return 1.0
            visited.add(src)
            for neighbor, value in graph[src].items():
                if neighbor not in visited:
                    result = dfs(neighbor, dst, visited)
                    if result != -1.0:
                        return value * result
            return -1.0
        
        # Step 3: Process each query using the graph
        results = []
        for C, D in queries:
            results.append(dfs(C, D, set()))
        
        return results
