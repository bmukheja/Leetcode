from typing import List

class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        output = set()
        n = len(nums)
        nums.sort()
        for i in range(n-2):
            j,k = i+1, n-1
            while j<k:
                if nums[j]+nums[k] == -nums[i]:
                    output.add((nums[i],nums[j],nums[k]))
                    while j < k and nums[j] == nums[j + 1]:
                        j += 1
                    while j < k and nums[k] == nums[k - 1]:
                        k -= 1
                    j += 1
                    k -= 1
                elif nums[j]+nums[k] > -nums[i]:
                    k-=1
                else:
                    j+=1
        return [list(item) for item in output]



print(Solution().threeSum([-1, 0, 1, 2, -1, -4]))