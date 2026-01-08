"""
Docstring for LinkedList.doublyLL

Doubly LL: 
- The main advantage of a doubly linked list is that it allows for efficient traversal of the list in both directions. 
- This is because each node in the list contains a pointer to the previous node and a pointer to the next node.
"""

class Node:
    def __init__(self, data):
        self.data = data
        self.prev = None
        self.next = None

"""
Traversal: forward, backward
"""

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

"""
Insertion: Beginning, End, Specific Position
"""

def insert_at_front(head, new_data):
    new_node = Node(new_data)
    new_node.next = head
    if head is not None:
        head.prev = new_node
    return new_node

def insert_at_end(head, new_data):
    new_node = Node(new_data)
    if head is None:
        head = new_node
    else:
        curr = head
        while curr.next is not None:
            curr = curr.next
        curr.next = new_node
        new_node.prev = curr
    return head

def insert_at_pos(head, pos, new_data):
    new_node = Node(new_data)
    # insert at the beginning
    if pos == 1:
        new_node.next = head
        if head is not None:
            head.prev = new_node
        head = new_node
        return head
    curr = head
    for i in range(1, pos-1):
        if curr is None:
            break
        curr = curr.next
    if curr is None:
        return head
    new_node.prev = curr
    new_node.next = curr.next



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