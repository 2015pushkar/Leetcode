"""
Docstring for LinkedList.removeDuplicates
- In order to remove duplicates from a LL, we need to be able to track duplicates
- A simple hash table would work
- We can do all this in one pass itself
"""

# a linked list node
class Node:

    # constructor to initialize a new node with data
    def __init__(self, data):
        self.data = data
        self.next = None

def deleteDups(head):
    # 10->20->20->20->30->40
    #     p   c 
    # seen = {10, 20}
    # prev.next = curr.next => is not moving prev ptr, it only makes sure that the first 20 is pointing to the third 20
    # 10->20->20->30->40
    #     p   c 
    seen = set()
    prev = None
    curr = head
    while curr:
        if curr.data in seen:
            prev.next = curr.next
            curr = curr.next
        else:
            seen.add(curr.data)
            prev = curr
            curr = curr.next
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

    # create a hard-coded linked list:
    # 10 -> 20 -> 30 -> 40
    head = Node(10)
    head.next = Node(20)
    head.next.next = Node(20)
    head.next.next.next = Node(20)
    head.next.next.next.next = Node(30)
    head.next.next.next.next.next = Node(40)

    head = deleteDups(head)

    printList(head)
    