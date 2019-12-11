from typing import List

class Solution:
    def findMin(self, nums: List[int]) -> int:
        l, r = 0, len(nums) - 1

        while l < r:
            mid = (l + r) // 2
            if nums[mid] > nums[mid + 1]:
                return nums[mid + 1]
            elif nums[mid] > nums[-1]:
                l = mid + 1
            else:
                r = mid
        return nums[0]


print(Solution().findMin([4,5,6,7,0,1,2]))
