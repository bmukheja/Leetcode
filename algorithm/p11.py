from typing import List

class Solution:
    def maxArea(self, height: List[int]) -> int:
        """
        Put pointers at start and end.
        Whichever is shorter, move that pointer
        """
        n = len(height)
        start,end = 0,n-1
        maxarea = 0
        while start!=end:
            area = min(height[end],height[start]) * (end - start)
            if area>maxarea:
                maxarea = area
            if height[start]<height[end]:
                start+=1
            else:
                end-=1

        return maxarea


print(Solution().maxArea([1,8,6,2,5,4,8,3,7]))