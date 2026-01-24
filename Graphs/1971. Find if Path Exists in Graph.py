"""
Docstring for Graphs.1971. 1971. Find if Path Exists in Graph
- Undirected graph
- Adjancency list needs to be created
- edges length max can be 2*10**5 - be careful about recursive dfs, we might end up reaching recursion depth

Given:
- n = 3, edges = [[0,1],[1,2],[2,0]], source = 0, destination = 2
- output: true/false
"""
from collections import deque

def validPath_bfs(n: int, edges: list[list[int]], source: int, destination: int) -> bool:
    if source == destination:
        return True
    
    # Build adjacency list (undirected)
    adj = [[] for _ in range(n)]
    for u,v in edges:
        adj[u].append(v)
        adj[v].append(u)

    visited = [False]*n
    q = deque([source])
    visited[source] = True

    while q:
        u = q.popleft()
        for v in adj[u]:
            if not visited[v]:
                if v == destination:
                    return True
                visited[v] = True
                q.append(v)
    return False

# Quick sanity tests
print(validPath_bfs(3, [[0, 1], [1, 2], [2, 0]], 0, 2))          # True
print(validPath_bfs(6, [[0, 1], [0, 2], [3, 5], [5, 4], [4, 3]], 0, 5))  # False