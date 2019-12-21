from typing import List

class Solution:
    def rob(self, nums: List[int]) -> int:
        """
        In the dp array, For every house, store the max money it will have if he rob that house
        Return the max of last two houses
        """
        if len(nums)==0:
            return 0
        if len(nums)==1:
            return nums[0]

        last,now = 0,0

        for i in nums:
            last,now = now,max(last+i,now)

        return now

assert Solution().rob([1,2,3,1]) == 4
assert Solution().rob([2,7,9,3,1]) == 12