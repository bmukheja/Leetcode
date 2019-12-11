# coding=utf-8
class Solution(object):
    def containsNearbyDuplicate(self, nums, k, t):
        """
        :type nums: List[int]
        :type k: int
        :rtype: bool
        """
        # from collections import defaultdict
        for i, v in enumerate(nums):
            for v2 in nums[i:i+k+1]:
                if abs(v - v2)<=t:
                    return True
        return False
