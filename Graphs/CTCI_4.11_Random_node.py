"""
- Implement a binary search tree (BST) class
- methods: insert(), find(), delete(), getRandomNode()
- Solution:
    - 1. (Slow & Working) Copy all the nodes to an array and return a random element in the array, T.C: O(N), S.C: O(N)
    - 2. (Slow & Working) Maintain an array at all times that lists the nodes in the tree. The problem is that we will need to remove nodes from this array as we delete them from the tree, T.C: O(N), S.C: O(N)
    - 3. (Slow & Working) Label all the nodes with an index from 1 to N and label them in a Binary search order (that is according to its in-order traversal).
            - Then we call the getRandomNode(), generate the random index between 1 to N.
            - We can use a BST to find its index
            - Issue: Insert a node or delete it, all of the indices needs to be updated.
            - T.C: O(N)
    - 4. - Know the Depth of the tree,
        - pick a random depth and traverse left/right randomly until we go to that depth. All nodes are not necessarily equally likely chosen
    - 5.
"""

# Solution 3:
"""
- After every insert/delete do an in-order traversal and assign each node an index (rank) from 1...N
- getRandomNode():
    1. Assign indices 1...N in inorder order and label them in BST order
    1. pick random k from [1...N]
    2. search the tree left and right for the k value
    
        10(4)
       /     \
    5(2)     15(5)
    /  \
 3(1)  7(3)

Visual path:
        10(4)
       /     
    5(2)     
      \
      7(3)   

"""

import random
from typing import Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def insertIntoBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        if not root:
            return TreeNode(val)
        if val <= root.val:
            if root.left is None:
                root.left = TreeNode(val)
            else:
                self.insertIntoBST(root.left, val)
        else:
            if root.right is None:
                root.right = TreeNode(val)
            else:
                self.insertIntoBST(root.right, val)
        return root

    def searchBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        #         B.C
        if root is None:
            return None
        if root.val == val:
            return root
        #  Recursive case
        if val<root.val:
            return self.searchBST(root.left, val)
        else:
            return self.searchBST(root.right, val)

    def getRandomNode(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if not root:
            return None
        n = self.count_nodes(root)
        k = random.randint(1,n)   # random inorder index (1..N)
        return self.kth_inorder(root, k) # find node with that inorder index

    def count_nodes(self, node: Optional[TreeNode]) -> int:
        if not node:
            return 0
        return 1 + self._count_nodes(node.left) + self._count_nodes(node.right)

    def kth_inorder(self, root: TreeNode, k: int) -> TreeNode:
        stack = []
        cur = root

        while stack or cur:
            while cur:
                stack.append(cur)
                cur = cur.left

            cur = stack.pop()
            k -= 1
            if k == 0:
                return cur

            cur = cur.right

        # should never happen if k is valid
        return root

# Solution 4:
# Option #4 (Fast but NOT uniform) — Why it fails (example)
#
# Example BST:
#         10
#        /  \
#       5    15
#      / \
#     3   7
#    /
#   2
#
# Algorithm:
# 1) Pick random depth d uniformly from {0,1,2,3}  -> P(d)=1/4 each
# 2) Walk down d steps choosing Left/Right with prob 1/2 each
# 3) If chosen child is NULL before reaching depth, STOP and return current node
#
# Compute returned-node probabilities:
# d=0: return 10
#   P(10) += 1/4
#
# d=1: one step from 10
#   10->L => 5 : (1/4)*(1/2) = 1/8
#   10->R => 15: (1/4)*(1/2) = 1/8
#
# d=2:
#   10->L->L => 3 : (1/4)*(1/2)*(1/2) = 1/16
#   10->L->R => 7 : (1/4)*(1/2)*(1/2) = 1/16
#   10->R (hits leaf 15, next step NULL) => return 15: (1/4)*(1/2) = 1/8
#
# d=3:
#   10->R (15 is leaf, next steps NULL) => return 15: (1/4)*(1/2) = 1/8
#   10->L->R (7 is leaf, step3 NULL)    => return 7 : (1/4)*(1/2)*(1/2) = 1/16
#   10->L->L then:
#       step3 Left  => 2 : (1/4)*(1/2)*(1/2)*(1/2) = 1/32
#       step3 Right => NULL => return 3: (1/4)*(1/2)*(1/2)*(1/2) = 1/32
#
# Final distribution:
# P(10)=1/4
# P(5) =1/8
# P(15)=1/8 + 1/8 + 1/8 = 3/8  (biased HIGH due to early stops)
# P(7) =1/16 + 1/16 = 1/8      (returned at d=2 and also at d=3 when stuck)
# P(3) =1/16 + 1/32 = 3/32 (The extra 1/32 comes from the d = 3 case when you almost go to node 2 but you pick the wrong direction at node 3 and hit null, so you stop and return 3.)
# P(2) =1/32
#
# Not uniform (uniform would be 1/6 each) -> hence "Fast & Not Working".

"""
Option #4
- First choose a target depth d.
- Then take exactly d steps (unless you hit null early).
- Bias happens because some branches are shorter / sparse → you “get stuck” and return shallow nodes more often (like 15).
- bias = uneven depth + early stopping.
"""

"""
Option #5
- No target depth.
- At every node, you roll a random choice:
- return current node
- go left
- go right
- Bias happens because the root gets a big “return immediately” chance, and deeper nodes require multiple “keep going” choices in a row.
- bias = “stop chance at every step” → shallow nodes dominate.
"""

# Option #5 (Fast but NOT uniform) — Why it fails
#
# Idea: The return mainly says I am choosing this node as my random node
# Randomly walk down the tree. At each node choose one action:
#   - With probability X: RETURN current node
#   - With probability X: GO LEFT
#   - With probability X: GO RIGHT
# (often X = 1/3 each, or any fixed constants; sometimes if chosen child is NULL, you stop/return too)
#
# Why it is biased:
# 1) Shallow nodes (especially the root) get much higher probability.
#    Example with X = 1/3 on this tree:
#         10
#        /  \
#       5    15
#      / \
#     3   7
#    /
#   2
#
#   P(10) = 1/3                          (return immediately at root)
#   P(5)  = (1/3)*(1/3)   = 1/9          (go left, then return)
#   P(3)  = (1/3)^3       = 1/27         (left, left, return)
#   P(2)  = (1/3)^4       = 1/81         (left, left, left, return)
#
#   Deeper nodes require multiple "keep going" choices in a row,
#   so their probability shrinks exponentially.
#
# 2) Root gets X probability by itself, and the entire left subtree also only gets X.
#    At root:
#      - Returning root uses probability X
#      - Entering left subtree uses probability X
#    So one node (root) can be as likely as ALL nodes in a whole subtree combined.
#
# Conclusion:
# Fast to run per step, but NOT equally likely across nodes -> not a valid uniform random node picker.


import random
from typing import Optional


class TreeNode:
    def __init__(self, data: int):
        self._data = data
        self.left: Optional["TreeNode"] = None
        self.right: Optional["TreeNode"] = None
        self._size = 1  # nodes in this subtree (including self)

    # ---- core methods (match the Java) ----
    def size(self) -> int:
        return self._size

    def data(self) -> int:
        return self._data

    def insert_in_order(self, d: int) -> None:
        if d <= self._data:
            if self.left is None:
                self.left = TreeNode(d)
            else:
                self.left.insert_in_order(d)
        else:
            if self.right is None:
                self.right = TreeNode(d)
            else:
                self.right.insert_in_order(d)
        self._size += 1

    def find(self, d: int) -> Optional["TreeNode"]:
        if d == self._data:
            return self
        if d <= self._data:
            return self.left.find(d) if self.left else None
        else:
            return self.right.find(d) if self.right else None

    def get_random_node(self) -> "TreeNode":
        left_size = self.left.size() if self.left else 0
        index = random.randrange(self._size)  # 0 .. size-1

        if index < left_size:
            return self.left.get_random_node()  # left must exist here
        elif index == left_size:
            return self
        else:
            return self.right.get_random_node()  # right must exist here

    # optional: nicer printing
    def __repr__(self) -> str:
        return f"TreeNode(data={self._data}, size={self._size})"


# ---- quick demo ----
if __name__ == "__main__":
    root = TreeNode(10)
    for x in [5, 15, 3, 7, 2]:
        root.insert_in_order(x)

    print("find(7):", root.find(7))
    print("random:", root.get_random_node())
