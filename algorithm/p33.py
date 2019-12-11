from typing import List

class Solution:
    def search(self, nums: List[int], target: int) -> int:
        if not nums:
            return -1
        l, r = 0, len(nums) - 1
        start = 0
        while l < r:
            mid = (l + r) // 2
            if nums[mid] > nums[mid + 1]:
                start = mid + 1
                break
            elif nums[mid] > nums[-1]:
                l = mid + 1
            else:
                r = mid

        if target==nums[start]:
            return start
        l,r = 0, len(nums)-1
        while l<r:
            mid = (l+r)//2
            realmid = (mid+start)%len(nums)

            if nums[realmid]==target:
                return realmid
            elif nums[realmid]<target:
                l=mid+1
            else:
                r=mid
        return -1


print(Solution().search([4,5,7,0,1,2],3))