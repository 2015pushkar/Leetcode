"""
- Create LL of all the nodes at each depth
- If you have a tree with depth D, you will have D linked lists
Implementation:
    - Collect node at the same depth into one chain like structure
    - python does not have a built-in LL, collections.deque is the closest std library that behaves like a LL for appends
    - So output is like:
        - depth 0: nodes at root level
        - depth 1: nodes one edge away
        - depth 2: nodes two edges away
and so on.

- DFS solution:
    - T.C: O(N)
    - S.C: O(logN) recursive calls - each adds a new level to the stack; For a skewed tree worst case O(N)
- BFS solution:
    - T.C: O(N)
    - S.C: O(W), where W is the maximum width of the tree, for a balanced tree W = N/2, so worst case O(N)

- Neither is always better,
    - Balanced tree, DFS recursion tends to use less auxiliary memory O(logN) than BFS
    - Skewed tree, BFS tends to use less auxiliary memory than DFS recursion

- One practical detail, Deep recursion can crash due to recursion limit, even if the big O looks fine. Iterative BFS avoids that issue.
"""

from collections import deque
from dataclasses import dataclass
from typing import Deque, List, Optional

# assumes you already have TreeNode defined:
@dataclass
class TreeNode:
    val: int
    left: Optional["TreeNode"] = None
    right: Optional["TreeNode"] = None

def list_of_depths_dfs(root: Optional["TreeNode"]) -> List[Deque["TreeNode"]]:
    lists: List[Deque["TreeNode"]] = []

    def helper(node: Optional["TreeNode"], level: int) -> None:
        # TODO 1: base case
        if node is None:
            return
        # TODO 2: if this is the first time we reached this level, add a new deque
        if len(lists) == level:
            lists.append(deque())
        # TODO 3: add node to its level deque
        lists[level].append(node)
        # TODO 4: recurse left then right with level + 1
        helper(node.left, level + 1)
        helper(node.right, level + 1)


    helper(root, 0)
    return lists


def list_of_depths_bfs(root: Optional["TreeNode"]) -> List[Deque["TreeNode"]]:
    result: List[Deque["TreeNode"]] = []

    # TODO 1: initialize current level deque with root if root exists
    current = deque()
    if root is not None:
        current.append(root)

    # TODO 2: while current is not empty:
    #         add current to result
    #         build next level deque from children of nodes in current
    #         set current to next level
    while current:
        result.append(current)
        parents = current
        current = deque()
        for parent in parents:
            if parent.left:
                current.append(parent.left)
            if parent.right:
                current.append(parent.right)

    return result

from collections import deque

def levels_to_vals(levels):
    return [[node.val for node in level] for level in levels]

def run_tests():
    # Test 1: empty tree
    root = None
    out = list_of_depths_dfs(root)
    assert levels_to_vals(out) == [], f"Empty tree failed: {levels_to_vals(out)}"

    # Test 2: single node
    root = TreeNode(1)
    out = list_of_depths_dfs(root)
    assert levels_to_vals(out) == [[1]], f"Single node failed: {levels_to_vals(out)}"

    # Test 3: perfect balanced tree
    #        1
    #      2   3
    #     4 5 6 7
    root = TreeNode(
        1,
        TreeNode(2, TreeNode(4), TreeNode(5)),
        TreeNode(3, TreeNode(6), TreeNode(7)),
    )
    out = list_of_depths_dfs(root)
    assert levels_to_vals(out) == [[1], [2, 3], [4, 5, 6, 7]], f"Perfect tree failed: {levels_to_vals(out)}"

    # Test 4: left skewed
    #    1
    #   2
    #  3
    # 4
    root = TreeNode(1, TreeNode(2, TreeNode(3, TreeNode(4))))
    out = list_of_depths_dfs(root)
    assert levels_to_vals(out) == [[1], [2], [3], [4]], f"Left skewed failed: {levels_to_vals(out)}"

    # Test 5: right skewed
    # 1
    #  2
    #   3
    #    4
    root = TreeNode(1, None, TreeNode(2, None, TreeNode(3, None, TreeNode(4))))
    out = list_of_depths_dfs(root)
    assert levels_to_vals(out) == [[1], [2], [3], [4]], f"Right skewed failed: {levels_to_vals(out)}"

    # Test 6: uneven with missing children
    #        1
    #      2   3
    #       4    5
    root = TreeNode(
        1,
        TreeNode(2, None, TreeNode(4)),
        TreeNode(3, None, TreeNode(5)),
    )
    out = list_of_depths_dfs(root)
    assert levels_to_vals(out) == [[1], [2, 3], [4, 5]], f"Uneven failed: {levels_to_vals(out)}"

    # Test 7: deeper uneven
    #        1
    #      2   3
    #     4     5
    #      6
    root = TreeNode(
        1,
        TreeNode(2, TreeNode(4, None, TreeNode(6)), None),
        TreeNode(3, None, TreeNode(5)),
    )
    out = list_of_depths_dfs(root)
    assert levels_to_vals(out) == [[1], [2, 3], [4, 5], [6]], f"Deeper uneven failed: {levels_to_vals(out)}"

    print("All DFS tests passed!")

run_tests()

