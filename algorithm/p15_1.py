class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        """Brute force solution uses a sorted list and 3 pointers O(n^2) and uses optimization to skip duplicates"""
        nums = sorted(nums)
        pairs = []
        n = len(nums)
        for i in range(n-2):
            if nums[i]>0:
                break
            if i>0 and nums[i]==nums[i-1]:
                continue
            l = i+1
            r = n-1

            while l<r:
                s = nums[l]+nums[r]+nums[i]
                if s==0:
                    pairs.append([nums[i],nums[l],nums[r]])
                    while l<r and nums[l]==nums[l+1]:
                        l+=1
                    while l<r and nums[r]==nums[r-1]:
                        r-=1
                    l+=1
                    r-=1
                elif s<0:
                    l+=1
                elif s>0:
                    r-=1
        return pairs