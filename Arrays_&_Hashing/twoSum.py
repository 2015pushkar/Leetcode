def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen = {}
        for i,val in enumerate(nums):
            diff = target - val 
            if diff in seen:
                return [seen[diff],i]
            seen[val] = i
        return []

'''
Here we use dictionaries to keep track of the numbers we have seen so far and their indices.
This allows us to find the two numbers that add up to the target in a single pass through the list.
'''