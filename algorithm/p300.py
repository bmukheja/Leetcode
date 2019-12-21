from typing import List

class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        if nums == []:
            return 0
        dp = [1]*len(nums)
        max_till_now = 0
        for i in range(1,len(nums)):
            for j in range(0,i):
                if nums[j]<nums[i]:
                    dp[i] = max(dp[i],dp[j]+1)
            max_till_now = max(max_till_now,dp[i])
        return max_till_now

print(Solution().lengthOfLIS([1,3,6,7,9,4,10,5,6]))