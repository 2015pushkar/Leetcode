# Detect Cycle in Linked List
"""
A cycle exists if, while traversing the list through next pointers, 
You encounter a node that has already been visited instead of eventually reaching nullptr
"""

"""
- Use a hashset, while traversing the node
- Whenever a node is encountered that is already present in the hashset
(Which indicates there's a cycle (loop) in the list) then return true
- If the node is NULL, represents the end of Linked List, return false as there is no loop
"""
class Node:
    def __init__(self, x):
        self.data = x
        self.next = None

# Using HashSet: O(n) time and O(n) Space

def detectLoop(head):
    seen = set()
    while head is not None:
        # if this node is already present in the hashmap it means there is a cycle
        if head in seen:
            return True
        # if we are seeing the node for the first time, insert it in hash
        seen.add(head)
        head = head.next
    return False

# [Expected Approach] Using Floyd's Cycle-Finding Algorithm
# It uses two pointers slow and fast, fast pointer move two steps ahead and slow will move one step ahead at a time.
# Traverse linked list using two pointers
# Move one pointer (slow) by one step ahead and another pointer (fast) by two steps ahead.
# If these pointers meet at the same node then there is a loop.
# If pointers do not meet then the linked list doesn't have a loop.

"""
Why meeting is guaranteed if a cycle exists ?
A: Let: m = number of nodes before the cycle starts and c = length of the cycle (number of nodes in the loop)
- Every iteration fast ptr gains one step extra then the slow pointer.
- The distance between the slow and fast ptr is d = (F − S)
- The cycle has c nodes and once you are in the cycle, the positions wrap around Positions: 0 → 1 → 2 → 3 → 4 → back to 0
- so positions are computed as (position mod c)
- d0 be the initial distance, slow moves 1 and fast moves 2; (2-1)=1
- After K iterations, distance = (d0 + k)%c; Distance 0 means: Fast and Slow ptr are at the same node


-- Interviwer ready answer:
- Once both pointers enter the cycle, the slow pointer moves 1 step and the fast pointer moves 2 steps.
- So in every iteration, the fast pointer gains one extra step on the slow pointer.
- Because the cycle has a fixed length c, positions inside the cycle wrap around.
- So the distance between the fast and slow pointers keeps increasing by 1 but modulo c.
- That means the distance will eventually become 0, which implies both pointers land on the same node.
- Since there are only c possible positions in the cycle, this must happen within at most c steps.
- Therefore, if a cycle exists, the fast and slow pointers are guaranteed to meet.
"""

def detectLoop_Floyd(head):
    """
    Docstring for detectLoop_Floyd
    T.C: O(n)
    S.C: O(1)
    """
    # fast and slow pointer initially points to the same head
    slow = head
    fast = head

    while fast and slow and fast.next:
        slow = slow.next
        fast = fast.next.next

        # if fast and slow ptr points to the same node, then the cycle is detected
        if slow == fast:
            return True
    return False



if __name__ == "__main__":
    head = Node(1)
    head.next = Node(3)
    head.next.next = Node(4)
    head.next.next.next = head.next

    if detectLoop(head):
        print("True using hash")
    else:
        print("False using hash")

    if detectLoop_Floyd(head):
        print("True using Floyd")
    else:
        print("False using Floyd")



