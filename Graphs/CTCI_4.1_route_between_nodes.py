"""
- Solvew either by DFS/BFS. Mark the node that is already visited to avoid cycles and repetition of the nodes.
1. BFS: 
    - Unvisited, Visited, Visiting
"""
from enum import Enum
from collections import deque
from typing import Dict, List, Hashable

class State(Enum):
    UNVISITED = 0
    VISITING = 1
    VISITED = 2


def has_path_bfs(graph, start, end) -> bool:
    """
    BFS(graph, start, end):
    if start == end: return True

    for each node u in graph:
        state[u] = UNVISITED

    state[start] = VISITING
    queue = new Queue()
    queue.enqueue(start)

    while queue not empty:
        u = queue.dequeue()

        for each v in neighbors(u):
            if state[v] == UNVISITED:
                if v == end: return True
                state[v] = VISITING
                queue.enqueue(v)

        state[u] = VISITED

    return False

    """
    if start == end:
        return True

   # Initialize UNVISITED state for all nodes that appear as keys or neighbors 
    all_nodes = set(graph.keys())
    for nbrs in graph.values():
        all_nodes.update(nbrs)
    state = {node: State.UNVISITED for node in all_nodes}

    q = deque([start])
    state[start] = State.VISITING

    while q:
        u = q.popleft()

        for v in graph.get(u, []):
            if state[v] == State.UNVISITED:
                if v == end:
                    return True
                state[v] == state.VISITING
                q.append(v)
        state[u] == State.VISITED
    return False

def has_path_dfs(graph, start, end) -> bool:
    if start == end:
        return True
    all_nodes = set(graph.keys())
    for nbrs in graph.values():
        all_nodes.update(nbrs)
    state = {node: State.UNVISITED for node in all_nodes}

    def dfs(u) -> bool:
        if u == end:
            return True
        state[u] == State.VISITING

        for v in graph.get(u, []):
            if state[v] == State.UNVISITED:
                if dfs(v):
                    return True
        state[u] = State.VISITED
        return False

    return dfs(start)

"""
Trade-offs between BFS and DFS: 
- DFS is simpler to implement, but may traverse one adjacent node very deeply before ever going onto the immediate neighbors.
- BFS is useful for finding the shortest path
"""





graph = {0: [1,2], 1:[3], 2:[], 3:[]}
start = 0
end = 3
print(has_path_bfs(graph, start, end))
