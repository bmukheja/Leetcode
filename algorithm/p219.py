class Solution(object):
    def containsNearbyDuplicate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: bool
        """
        collection = {}
        for i in range(len(nums)):
            if nums[i] in collection and i -collection[nums[i]] <= k:
                return True
            else:
                collection[nums[i]] = i
        return False