# a linked list node
class Node:

    # constructor to initialize a new node with data
    def __init__(self, data):
        self.data = data
        self.next = None

def helper(node, n):
    if node is None:
        return 0, None

    count, ans = helper(node.next, n)
    count += 1

    if count == n:
        ans = node.data

    return count, ans


    

    
if __name__ == "__main__":

    # create a hard-coded linked list:
    # 10 -> 20 -> 30 -> 40
    head = Node(10)
    head.next = Node(20)
    head.next.next = Node(30)
    head.next.next.next = Node(40)
    head.next.next.next.next = Node(50)
    head.next.next.next.next.next = Node(60)

    n=2

    print(helper(head, 2))
    