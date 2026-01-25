"""
Docstring for Graphs.CTCI_Minimal_Tree
- Algorithm to create a BST with minimal height
- To create a minimal tree, we need to match the 
- #nodes left subtree to the #nodes in the right sub-tree as much as possible.
- root will be the middle of the array. half the elements are less than the root and half would be greater then the root.
- insert into the tree the middle element of the array
- insert (into the left subtree) the left subarray elements
- insert (into the right subtree) the right subarray elements
- Recurse
"""
from dataclasses import dataclass

@dataclass
class TreeNode:
    val: int
    left: 'TreeNode' = None
    right: 'TreeNode' = None

def create_minimal_bst(arr: list[int]) -> TreeNode:
    def build(start: int, end: int) -> TreeNode:
        if end<start:
            return None
        mid = (start + end) // 2
        node = TreeNode(arr[mid])
        node.left = build(start, mid - 1)
        node.right = build(mid + 1, end)
        return node
    return build(0, len(arr)-1)

# Helper: inorder traversal should return sorted array if BST is correct
def inorder(root: TreeNode) -> list[int]:
    if not root:
        return []
    return inorder(root.left) + [root.val] + inorder(root.right)

# Helper: level-order print (to visualize structure)
from collections import deque
def level_order(root: TreeNode) -> list[list[int]]:
    if not root:
        return []
    res = []
    q = deque([root])
    while q:
        level = []
        for _ in range(len(q)):
            node = q.popleft()
            level.append(node.val)
            if node.left: q.append(node.left)
            if node.right: q.append(node.right)
        res.append(level)
    return res

if __name__ == "__main__":
    arr = [1, 2, 3, 4, 5, 6, 7]
    root = create_minimal_bst(arr)
    print("inorder:", inorder(root))        # [1,2,3,4,5,6,7]
    print("levels:", level_order(root))     # [[4],[2,6],[1,3,5,7]]



