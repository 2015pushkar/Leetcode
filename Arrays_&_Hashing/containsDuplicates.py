def containsDuplicate(self, nums: List[int]) -> bool:
        hashset = set()
        for num in nums:
            if num in hashset:
                return True
            hashset.add(num)
        return False

'''
Here we use a set to keep track of the numbers we have seen so far.
If we encounter a number that is already in the set, we know there is a duplicate.
This allows us to check for duplicates in a single pass through the list.
'''