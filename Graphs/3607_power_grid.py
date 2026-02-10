"""
connections u -> v
queries: maintenance is required for station x
    - [1,x]: if x is online: resolves itself else if x is offline, check is resolved by operational station with the smallest id else return -1
    - [2,x]: station x goes offline

- A connected component is a “cluster” of stations where every station can reach every other station through edges.

Input: c = 5,
connections = [[1,2],[2,3],[3,4],[4,5]], -> convert to adjacency list
queries = [[1,3],[2,1],[1,1],[2,2],[1,2]]

- [1,3] -> check if 3 is online -> 3
- [2,1] -> (1 is offline) -> None
- [1,1] -> 1 is offline, check for the operational station with the smallest id -> 2
- [2,2] -> 2 is offline -> None
- [1,2] -> 2 is offline -> 3

Hint:
    - Track the min value using min heap
    - Online hashset: Lazy delete from the hashset. If we want to populate an element from the minheap do it with the normal operation just do not consider elements that are offline (pop from the minheap - log(n) to push and pop)
    - If two connected components then each will have its own min-heap

Heap initially: [1, 2, 3, 4, 5] [6,7]
visited = {1,2,3,4,5}
station_group = {1:1, 2:1, 3:1, 4:1, 5:1, 6:2}
min_heaps[1] contains {1,2,3,4,5} (as a heap, top is 1)
"""
from collections import defaultdict
from typing import List
import heapq

class Solution:
    def processQueries(self, c: int, connections: List[List[int]], queries: List[List[int]]) -> List[int]:
        adj = defaultdict(list)
        for u,v in connections:
            adj[u].append(v)
            adj[v].append(u)

        online = set()
        station_group = {}
        min_heaps = defaultdict(list)

#       Precompute connected components DFS/BFS - DFS that will collect all nodes in one component
#       Why do we need components: If station x is offline, find the smallest operational station that can “cover it”.
#       The graph might be disconnected

        def dfs(station, group_id):
            if station in online:
                return
            online.add(station)
            station_group[station] = group_id
            heapq.heappush(min_heaps[group_id], station)

            for nei in adj[station]:
                dfs(nei, group_id)
        # build connected components
        for s in range(1, c+1):
            dfs(s, s)

        res = []
        for q_type, q_station in queries:
            if q_type == 1:
                if q_station in online:
                    res.append(q_station)
                    continue
                # station offline
                group_id = station_group[q_station]
                min_heap = min_heaps[group_id]
                while min_heap and min_heap[0] not in online:
                    heapq.heappop(min_heap)
                if min_heap:
                    res.append(min_heap[0])
                else:
                    res.append(-1)
            else:
                online.discard(q_station)


"""
- Let c = #stations, E = #connections, Q = #queries.
- Build adjacency list: O(E)
- DFS to find components: O(c + E)
- Build heaps (one heappush per station): O(c log c)
- Process queries:
    - Each query does set membership checks in O(1).
    - Type [2,x] uses discard: O(1).
    - Type [1,x] may heappop in a loop, but each station can be popped at most once total across all queries (lazy deletion).
    - Total pops ≤ c, each pop costs O(log c) → O(c log c) amortized.
So all queries combined: O(Q + c log c)
Total time: O(E + Q + c log c)
"""



