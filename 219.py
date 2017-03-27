# coding=utf-8
class Solution(object):
    def containsNearbyDuplicate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: bool
        """
        # from collections import defaultdict
        d = dict()
        l = len(nums)
        for i in range(l):
            if nums[i] in d and i - d[nums[i]] <= k:
                return True
            else:
                d[nums[i]] = i
        return False


s = Solution()
print(s.containsNearbyDuplicate([1,0,1,1],1))