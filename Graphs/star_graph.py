from collections import defaultdict, Counter

def find_center(terminals):
    """
    Implement: Iterate over the list - tuple unpacking src, dest
    """
    seen = defaultdict(int)
    for src, dest in terminals:
        seen[src]+=1
        seen[dest]+=1
    return max(seen, key=seen.get)

def find_center_counter(terminals):
    """
    Implement: prefer Counter, because it is purpose-built for counting hashable objects. It is efficient
    """
    count = Counter()
    for src, dest in terminals:
        count[src]+=1
        count[dest]+=1
    return count.most_common(1)[0][0]
    

terminals1 = [[1,2],[2,3],[4,2]]
terminals2 = [[1,2],[5,1],[1,3],[1,4]]

print(find_center_counter(terminals1))
print(find_center(terminals2))