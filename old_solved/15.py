from itertools import groupby, combinations

class Solution(object):
    def threeSum(self, nums):
        output = []
        length = len(nums)
        nums = sorted(nums)
        for i in range(length-2):
            if i>0 and nums[i]==nums[i-1]:
                continue
            l,r = i+1,length-1
            while l<r:
                s = nums[i]+nums[l]+nums[r]
                if s<0:
                    l+=1
                elif s>0:
                    r-=1
                else:
                    output.append([nums[i],nums[l],nums[r]])
                    while l<r and nums[l]==nums[l+1]:
                        l+=1
                    while l<r and nums[r]==nums[r-1]:
                        r-=1
                    l+=1;r-=1
        return output

sol = Solution()
startTime = dt.now()
print(sol.threeSum(test_str))
time1 = dt.now() - startTime