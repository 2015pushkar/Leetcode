from typing import List

def get_subsets(arr: List[int], index: int = 0) -> List[List[int]]:
    # Base case: we've gone past the last element
    if index == len(arr):
        return [[]]  # one subset: the empty set

    # Get subsets of the remaining elements
    all_subsets = get_subsets(arr, index + 1)

    item = arr[index]
    more_subsets: List[List[int]] = []

    # Clone each existing subset and add the current item
    for subset in all_subsets:
        new_subset = subset.copy() # 1. [], 2. [], [3], 3. [], [3], [2], [3,2]
        new_subset.append(item)  # 1. [3], 2. [2], [3,2], 3. [1], [3,1], [2,1], [3,2,1]
        more_subsets.append(new_subset) # 1. [[3]], 2. [[3,2], [2]], 3. [[1], [3,1], [2,1], [3,2,1]]

    # Merge and return
    all_subsets.extend(more_subsets)  # [[], [3], [2], [3,2], [1], [3,1], [2,1], [3,2,1]]
    return all_subsets


# Example
if __name__ == "__main__":
    print(get_subsets([1, 2, 3]))
