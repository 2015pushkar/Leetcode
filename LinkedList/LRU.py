"""
Docstring for LinkedList.LRU
LRU cache: Removes the item that has not been accessed for the longest time, when the cache is full
Ex: The browser tab that is idle for a long time, would be the first one close when the memory is low
capcity: 2
hashset = MRU {(4,4),(3,3)} LRU
Doubly LL: 
- The main advantage of a doubly linked list is that it allows for efficient traversal of the list in both directions. 
- This is because each node in the list contains a pointer to the previous node and a pointer to the next node.
"""

class Node:
    def __init__(self, data):
        self.data = data
        self.prev = None
        self.next = None

def forward_traversal(head):
    curr = head
    while curr is not None:
        print(curr.data, end=" ")
        curr = curr.next
    print()

def backward_traversal(tail):
    curr = tail
    while curr is not None:
        print(curr.data, end=" ")
        curr = curr.prev
    print()

if __name__ == "__main__":
    head = Node(10)
    # creating a next node and linking it to the head
    second = Node(20)
    head.next = second
    second.prev = head

    # Create and link the third node
    third = Node(30)
    second.next = third
    third.prev = second

    # # Create and link the fourth node
    # head.next.next.next = Node(40)
    # head.next.next.next.prev = head.next.next

     # Traverse the list forward and print elements
    # temp = head
    # while temp is not None:
    #     print(temp.data, end="")
    #     if temp.next is not None:
    #         print(" <-> ", end="")
    #     temp = temp.next

    forward_traversal(head)
    backward_traversal(third)