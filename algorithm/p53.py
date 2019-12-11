from typing import List
import sys

class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        """
        We optimize this problem by stating the subproblem as - if the subarray till now is positive,
        it will contribute to the next element, otherwise no
        """
        maxsum = nums[0]
        for i in range(1,len(nums)):
            if nums[i-1]>0:
                nums[i] += nums[i-1]
            maxsum = max(nums[i],maxsum)
        return maxsum