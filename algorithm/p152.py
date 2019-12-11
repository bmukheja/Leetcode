from typing import List
import sys

class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        """
        Subproblem - The subarray till the current element has the maximum product"""
        dp = [-sys.maxsize]*len(nums)
        dp[0] = nums[0]
        maxprod = dp[0]
        for i in range(1,len(nums)):
            if dp[i-1] > 1 or (dp[i-1]<0 and nums[i]<0):
                dp[i] = nums[i]*dp[i-1]
            else:
                dp[i] = nums[i]
            maxprod = max(maxprod,dp[i])
        return maxprod

print(Solution().maxProduct([-2,0,-1]))