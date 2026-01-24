class Node:
    def __init__(self, value):
        self.value = value
        self.adjacent = []   # list of neighbor Node objects
        self.visited = False

"""
A
↙ ↘
B   C
↘ ↙
D

"""

def dfs_search(root):
    if root is None:
        return

    # visit(root)
    print(root.value)

    root.visited = True

    for n in root.adjacent:
        if not n.visited:
            dfs_search(n)


# example usage
a = Node("A")
b = Node("B")
c = Node("C")
d = Node("D")

a.adjacent = [b, c]
b.adjacent = [d]
c.adjacent = [d]

dfs_search(a)  # prints nodes in DFS order starting from A
