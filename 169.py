# coding=utf-8
class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        major,count = nums[0],1
        for i in range(len(nums)):
            if count == 0:
                count +=1
                major = nums[i]
            elif major == nums[i]:
                count +=1
            else:
                count -= 1
            return major
