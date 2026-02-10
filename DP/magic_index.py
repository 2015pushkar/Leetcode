# 1. A[i] = i is the magic index
# 2. Values are not distinct

def magicSlow(arr) -> int:
    for i in range(len(arr)):
        if arr[i] == i:
            return i
    return -1

# Condition 1: Sorted + distinct
# A[mid] < mid; On the LHS values are always smaller than the index, A[i] != i
#  A[mid]>mid (search in left for the magic number)
"""
- In the distinct case, if A[mid] < mid, we said “magic index can’t be on the left.”
That relied on the fact that values must drop by at least 1 per step when moving left.

- With duplicates, values might not drop. They can stay the same.
So the left side might still “catch up” to the index and hit equality.
"""

def magic_fast_distinct(arr): # O(log(n)) T.C
    return _magic_fast_distinct(arr, 0 , len(arr)-1)

def _magic_fast_distinct(arr, start, end):
    if end < start:
        return -1
    mid = (start + end) // 2

    if arr[mid] == mid:
        return mid
    elif arr[mid] > mid: # Search in left
        return _magic_fast_distinct(arr, start, mid-1)
    elif arr[mid] < mid: return _magic_fast_distinct(arr, mid+1, end)

"""
The general pattern is that we compare mid Index and midValue for equality first. Then, if they are not
equal, we recursively search the left and right sides as follows:
• Left side: search indices start through Math.min(midlndex - 1, midValue ).
• Right side: search indices Math. max(midlndex + 1, midValue) through end.

1 2 2 2 3 4 7 8 9
0 1 2 3 4 5 6 7 8
0 m    e m

"""

def magic_index_duplicates(arr):
    return _magic_index_duplicates(arr, 0, len(arr)-1)

def _magic_index_duplicates(arr, start, end):
    if end < start: return -1
    midIndex = (start + end) // 2
    midValue = arr[midIndex]

    if arr[midIndex] == midValue: return midIndex

    #     search left
    leftIndex = min(midIndex-1, midValue)
    left = _magic_index_duplicates(arr, start, leftIndex)
    if left >= 0:
        return left

    # search right
    rightIndex = max(midIndex+1, midValue)
    right = _magic_index_duplicates(arr, rightIndex, end)

    return right



nums = [-10, -5, 0, 3, 7, 9, 12] # distinct
print(magic_fast_distinct(nums))

nums = [-10, -5, 2, 2, 2, 3, 4, 7, 9, 12]
print(magic_fast_distinct(nums))