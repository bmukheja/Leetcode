from typing import List

class Solution:
    def canJump(self, nums: List[int]) -> bool:
        """
        Greedy approach. Good index means it can reach the last element. Last element is always a good index.
        Now for the leftmost good index in the array, if an index before it can reach this good index,
        the index before is also a good index and a new potential leftmostGoodIndex.
        """
        if len(nums) == 0:
            return False
        n = len(nums)
        dp = [False] * (n)
        leftmostGoodIndex = n - 1
        for i in range(n - 2, -1, -1):
            if i + nums[i] >= leftmostGoodIndex:
                leftmostGoodIndex = i
                continue

        return True if leftmostGoodIndex == 0 else False