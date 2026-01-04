"""
Docstring for LinkedList.insertionLL
Insert a node at the beginning of the LL
- create a new node
- remove the head from the original first node of LL
- make the new node as the head of the LL
"""
class Node:
    def __init__(self, x):
        self.data = x
        self.next = None

# Function to insert a new node at the beginning of the list
# T.C to insert a node at the head position is O(1); S.C is O(1)
def insertAtFront(head, x):
    newNode = Node(x)
    newNode.next = head
    head = newNode
    return head

# Insert at end
"""
- Create a new node and set its next ptr as NULL since it will be the last node.
- Store the head reference in a temporary variable
- If the LL is empty, make the new node as the head and return
- Else traverse till the last node
- Change the next ptr of the last node to point to the new node
"""
def insertAtEnd(head, x):
    # T.C: O(n), S.C: O(1)
    newNode = Node(x)
    if head is None:
        return newNode
    # Store the head reference in a temporary variable.
    temp = head
    # traverse till the last node
    while temp.next is not None:
        temp = temp.next
    # Change the next pointer of the temp/last node to point to the new node
    temp.next = newNode
    return head

# Insert a node at a specific position in a LL
def insertAtPos(head, pos, val):
    if pos<1:
        return head
    # head will change if pos == 1
    if pos == 1:
        newNode = Node(val)
        newNode.next = head
        return newNode
    
    curr = head
    for i in range(1, pos-1):
        if curr is None:
            return head
        curr = curr.next

    # If position is greater than number of nodes
    if curr is None:
        return head
    
    newNode = Node(val)

    newNode.next = curr.next
    curr.next = newNode

    return head


def printList(head):
    curr = head
    while curr is not None:
        print(curr.data, end="")
        if curr.next is not None:
            print(" -> ", end="")
        curr = curr.next
    print() 

if __name__ == "__main__":
    # Create the linked list 3->4->5
    # head = Node(2)
    head = Node(3)
    head.next = Node(4)
    head.next.next = Node(5)

    # Insert a new node at
    # the front of the list
    head = insertAtFront(head, 1)
    head = insertAtPos(head, 2, 2)
    head = insertAtEnd(head, 6)


    # Print the updated list
    printList(head)
