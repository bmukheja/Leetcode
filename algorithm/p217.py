from typing import List

class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        return len(set(nums))<len(nums)

print(Solution().containsDuplicate(([1,2,3,1])))