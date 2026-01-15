"""
Docstring for stacks.nge1

nums1 = [4,1,2]
nums2 = [1,3,4,2]
nums1Idx = {4:0, 1:1, 2:2}

i at 0, nums2[i]=1 is in nums1Idx, scan right
j=1 value 3 is greater than 1, so next greater for 1 is 3
idx = nums1Idx[1] = 1, set res[1]=3

"""
from typing import List

class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        # O(n * m)
        nums1Idx = {n: i for i, n in enumerate(nums1)}
        res = [-1] * len(nums1)

        for i in range(len(nums2)):
            if nums2[i] not in nums1Idx:
                continue

            for j in range(i + 1, len(nums2)):
                if nums2[j] > nums2[i]:
                    idx = nums1Idx[nums2[i]]
                    res[idx] = nums2[j]
                    break

        return res
    
"""
nums1 = [4,1,2]
nums2 = [1,3,4,2]
         i
nge = {3:4, 1:3}
stack = [4, 3]
[1,0,4]
"""


class Solution:
    def nge1(self, nums) -> dict[int,int]:
        stack = []
        nge = {}
        i = 0
        n = len(nums)
        for i in range(n-1, -1, -1):
            while stack and nums[i] > stack[-1]:
                stack.pop()
            if stack:
                nge[nums[i]] = stack[-1]
            stack.append(nums[i])
        return nge

    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        """
        nums[ngeres] => answer to put in the new array
        """
        res = []
        store = self.nge1(nums2)
        for num in nums1:
            res.append(store.get(num, -1))
        return res

        
            
