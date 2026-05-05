class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        
        adj_list = defaultdict(list)

        for u,v in edges:
            adj_list[u].append(v)
            adj_list[v].append(u)
        
        visited = [0]*n
        
        def dfs(node):
            visited[node] = 1
            for nei in adj_list[node]:
                if not visited[nei]:
                    dfs(nei)
        
        #count components
        components = 0

        for node in range(n):
            if not visited[node]:
                components +=1
                dfs(node)
        
        return components