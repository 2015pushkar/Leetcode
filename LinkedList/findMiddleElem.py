class Node:
    def __init__(self,x):
        self.data = x
        self.next = None

def getLength(head):
    length = 0
    curr = head
    while curr:
        length += 1
        curr = curr.next
    return length

def getMiddle(head):
    length = getLength(head)

    # traverse till we reach half of the length
    midIndex = length // 2
    while midIndex:
        head = head.next
        midIndex -= 1
    return head.data

def getMiddle_hare_and_tortoise(head) -> int:
    slowptr = head
    fastptr = head

    while fastptr is not None and fastptr.next is not None:
        # move the fast pointer by two nodes
        fastptr = fastptr.next.next

        # move the slow pointer by one node
        slowptr = slowptr.next

    return slowptr.data



if __name__ == "__main__":
    head = Node(10)
    head.next = Node(20)
    head.next.next = Node(30)
    head.next.next.next = Node(40)
    head.next.next.next.next = Node(50)
    head.next.next.next.next.next = Node(60)

print(getMiddle_hare_and_tortoise(head))


