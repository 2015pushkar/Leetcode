from collections import deque, defaultdict
def valid_tree(n, edges):
    """
    -> No loops, every node needs to be connected for a tree
    -> for every node needs to be connected: run a dfs/bfs and check if every node is visited. #nodes = #visited nodes
    -> If any cycle in the undirected graph: break -> finding a visited neighbor that is not the parent

    """
    if len(edges) != n - 1: # cycle detection and disconnected graph detection
        return False


    def adjacency_dict(edges) -> dict:
        # build the adjancency list
        adj_dict = defaultdict(list)
        for src, dest in edges:
            adj_dict[src].append(dest)
            adj_dict[dest].append(src)
        return adj_dict
    

    def bfs(adj_dict, source):
        queue = deque([(source, -1)])
        visited = set([source])
        while queue:
            current, parent = queue.popleft()
            for neighbor in adj_dict[current]:
                if neighbor not in visited:
                    visited.add(neighbor)
                    queue.append((neighbor, current))
                # add a cycle detection logic for bfs
                elif neighbor != parent: # VISITED already but not my parent
                    # cycle detected
                    return False
        # check if the graph is connected or not
        return n == len(visited)
    
    def dfs(adj_dict, node): #recursive method
        visited = set()
        def dfs_helper(node, parent=None):
            visited.add(node)
            for neighbor in adj_dict[node]:
                if neighbor not in visited:
                    dfs_helper(neighbor, parent=node)
                elif parent is not None and neighbor != parent:
                    return False
        dfs_helper(node)
        return n == len(visited)




    adjacency_dictionary = adjacency_dict(edges)
    # return bfs(adjacency_dictionary, 0)
    return dfs(adjacency_dictionary, 0)




# Input 1: 
n = 5 
edges = [[0, 1], [0, 2], [0, 3], [1, 4]]
# Output: true.
print(valid_tree(n, edges))

# Input 2: 
n = 5 
edges = [[0, 1], [1, 2], [2, 3], [1, 3], [1, 4]]
# Output: false.
print(valid_tree(n, edges))