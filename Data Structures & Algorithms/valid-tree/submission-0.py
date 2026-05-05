class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        graph = [[] for _ in range(n)]

        for u,v in edges:
            graph[u].append(v)
            graph[v].append(u)
        
        visited = [0] * n
        def dfs(node, parent):
            if visited[node]:
                return False
            visited[node] = 1
            for nei in graph[node]:
                if nei == parent:
                    continue
                if not dfs(nei, node):
                    return False
            return True
       
        return dfs(0, -1) and sum(visited) == n