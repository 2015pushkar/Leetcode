from collections import defaultdict
from typing import List

def twoSum(nums: List[int], target: int) -> List[int]:
    hashmap = defaultdict(int)
#    Store the val (diff) along with its indices for the number from which we take the difference
    for i in range(len(nums)):
        diff = target - nums[i]
        if diff in hashmap:
            return [hashmap[diff], i]
        hashmap[nums[i]] = i
    return []




nums = [2, 7, 11, 15]
target = 9
print(twoSum(nums, target))

nums = [3,2,4]
target = 6
print(twoSum(nums, target))

nums = [3,3]
target = 6
print(twoSum(nums, target))