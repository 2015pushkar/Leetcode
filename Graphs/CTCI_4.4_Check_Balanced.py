"""
- Check if a Binary tree is balanced
- A balanced tree: height of the two subtrees of any node never differ by more than one.
- Recurse through the entire tree, and for each node compute the heights of each subtree.
"""
#  not efficient as getHeights is called repeatedly on the same nodes. T.C: O(NlogN) -> balanced tree, if skewed: O(n^2)
def getHeight(root) -> int:
    if root is None:
        return -1
    return 1 + max(getHeight(root.left), getHeight(root.right))

def isBalanced(root) -> bool:
    if root is None:
        return True
    heightDiff = abs(getHeight(root.left) - getHeight(root.right))
    if heightDiff > 1:
        return False
    else: # recurse - we need to verify if the height diff is <= 1 for left and right sub-tree as well
        return isBalanced(root.left) and isBalanced(root.right)

# Update: getHeight along with the height can check if the tree is balanced -> return error code if not balanced else return tree height if balanced.
def checkHeight(root) -> int:
    if root is None:
        return -1
    leftHeight = checkHeight(root.left)
    if leftHeight == float("-inf"): return float("-inf")
    rightHeight = checkHeight(root.right)
    if rightHeight == float("-inf"): return float("-inf")

    heightDiff = abs(leftHeight - rightHeight)
    if heightDiff > 1:
        return float("-inf") # found error -> pass it back
    else:
        return max(leftHeight, rightHeight)+1
def isBalanced2(root) -> bool:
    return checkHeight(root) != float("-inf")