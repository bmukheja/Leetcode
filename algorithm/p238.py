from typing import List

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        product_uptil = [1]*len(nums)
        product_after = [1]*len(nums)

        for i in range(1,len(nums)):
            product_uptil[i] = nums[i-1]*product_uptil[i-1]
        for i in range(len(nums)-2,-1,-1):
            product_after[i] = nums[i+1]*product_after[i+1]

        for i in range(len(nums)):
            nums[i] = product_after[i]*product_uptil[i]
        return nums

print(Solution().productExceptSelf([1,2,3,4]))