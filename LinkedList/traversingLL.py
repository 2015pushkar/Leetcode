# a linked list node
class Node:

    # constructor to initialize a new node with data
    def __init__(self, new_data):
        self.data = new_data
        self.next = None

# function to traverse and print the singly linked list
def traverseList(head):
    while head is not None:
        print(head.data, end="")
        if head.next is not None:   
            print(" -> ", end="")
        head = head.next

def traverseList_rec(head):
    if head is None:
        return
    print(head.data, end="")
    if head.next is not None:
        print("->", end="")
    traverseList_rec(head.next)

if __name__ == "__main__":

    # create a hard-coded linked list:
    # 10 -> 20 -> 30 -> 40
    head = Node(10)
    head.next = Node(20)
    head.next.next = Node(30)
    head.next.next.next = Node(40)

    traverseList_rec(head)