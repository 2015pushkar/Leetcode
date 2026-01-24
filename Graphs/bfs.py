from collections import deque

class Node:
    def __init__(self, value):
        self.value = value
        self.adjacent = []   # list of neighbor Node objects
        self.marked = False  # same as visited

def bfs_search(root):
    if root is None:
        return

    queue = deque()
    root.marked = True
    queue.append(root)  # enqueue  C

    while queue:
        r = queue.popleft()  # dequeue
        print(r.value)       # visit(r)

        for n in r.adjacent:
            if not n.marked:
                n.marked = True
                queue.append(n)

# create nodes
A = Node("A")
B = Node("B")
C = Node("C")
D = Node("D")
E = Node("E")
F = Node("F")
G = Node("G")

# add edges (directed)
A.adjacent = [B, C]
B.adjacent = [D, E]
C.adjacent = [F]
E.adjacent = [G]
F.adjacent = [G]
D.adjacent = []
G.adjacent = []

bfs_search(A)  # prints nodes in DFS order starting from A

"""
      A
    ↙   ↘
   B     C
  ↙ ↘     ↓
 D   E     F
      ↘   ↙
        G

"""

