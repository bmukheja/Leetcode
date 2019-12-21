from typing import List

class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums)==0:
            return 0
        elif len(nums)==1:
            return nums[0]
        return max(self.helper(nums,0,len(nums)-1),self.helper(nums,1,len(nums)))

    def helper(self, nums: List[int], left,right) -> int:
        """
        In the dp array, For every house, store the max money it will have if he rob that house
        Return the max of last two houses
        """

        last,now = 0,0

        for i in nums[left:right]:
            last,now = now,max(last+i,now)

        return now




print(Solution().rob([2,3,2]),3)
print(Solution().rob([1,2,3,1]), 4)