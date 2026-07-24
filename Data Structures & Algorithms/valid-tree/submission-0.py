class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        # create adjacency list
        graph = defaultdict(list)
        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)
        
        visited = set()
        def dfs(curr, prev):
            if curr in visited:
                return False
            visited.add(curr)
            for neighbour in graph[curr]:
                if neighbour == prev:
                    continue
                if not dfs(neighbour, curr):
                    return False

            return True

        return dfs(0,-1) and len(visited) == n



