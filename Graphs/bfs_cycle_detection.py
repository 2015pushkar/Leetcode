from collections import deque

def bfs_cycle_detection(graph, source):
    queue = deque([(source, -1)])  # (node, parent)
    visited = set([source])

    while queue:
        node, parent = queue.popleft()
        for neighbor, connected in enumerate(graph[node]):
            if connected:  # edge exists
                if neighbor not in visited:
                    visited.add(neighbor)
                    queue.append((neighbor, node))
                elif neighbor != parent:
                    # Found a visited neighbor that is not the parent → cycle
                    return True
    return False

graph = [
    [0, 1, 0, 0, 1],
    [1, 0, 1, 1, 0],
    [0, 1, 0, 1, 0],
    [0, 1, 1, 0, 1],
    [1, 0, 0, 1, 0]
]

print(bfs_cycle_detection(graph, 0))  # Output: True

"""
        2
        │
        │
0 ───── 1 ───── 3 ───── 4
│              ╱        │
│            ╱          │
└────────── 4 ──────────┘

"""
