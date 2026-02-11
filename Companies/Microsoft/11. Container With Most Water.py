from typing import List
def maxArea(height: List[int]) -> int:
    """
    1. Algorithm 1: Brute-force. T.C: O(n^2), S.C: O(1)
    - enumerate nested for loops
    - maxArea inorder to calculate the area
    - i-> contract the containers, j-> to extend the window of the containers

    """
    # n = len(height)
    # maxArea = float('-inf')
    # for i in range(n):
    #     for j in range(i+1, n):
    #         area = (j-i)*min(height[i], height[j])
    #         maxArea = max(maxArea, area)
    # return maxArea

    """
    2. Algorithm 2: [1,8,6,2,5,4,8,3,7]
                       i             j   
    maxArea = 49
    T.C: O(n), S.C: O(1)
    """
    n = len(height)
    maxArea = float('-inf')
    left, right = 0, n-1
    area = 0
    while left<right:
        area = (right-left)*min(height[left],height[right]) 
        maxArea = max(maxArea, area)
        if height[left]<=height[right]:
            left+=1
        elif height[left]>height[right]:
            right-=1
        # else: # height[left] == height[right]
        #     left+=1
    return maxArea
    





height = [1,8,6,2,5,4,8,3,7]
print(maxArea(height))