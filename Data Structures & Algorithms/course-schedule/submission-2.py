class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        graph = defaultdict(list)

        for a,b in prerequisites:
            graph[a].append(b)

        # to prove that graph is acyclic
        seen = [0]*numCourses
        def dfs(node: int):
            # cycle detected
            if seen[node]:
                return False
            # optimize for no prerequisite
            if graph[node] == []:
                return True
            #mark visited
            seen[node] = 1
            for next_node in graph[node]:
                if not dfs(next_node):
                    return dfs(next_node)
            # backtrack
            seen[node] = 0
            # optimization to avoid further travel
            graph[node] = []
            return True
        # courses can be disconnected
        # do not assume a fully connected graph by default
        for c in range(numCourses):
            if not dfs(c):
                return False
        return True