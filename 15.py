from itertools import groupby, combinations

class Solution(object):
    def threeSum(self, nums):
        output = []
        length = len(nums)
        nums = sorted(nums)
        for i in range(length-2):
            if i>0 and nums[i]==nums[i-1]:
                continue
            for j in range(i+1,length-1):
                if j>i+1 and nums[j]==nums[j-1]:
                    continue
                for k in range(j+1,length):
                    if k>j+1 and nums[k]==nums[k-1]:
                        continue
                    if nums[i]+nums[j]+nums[k] == 0:
                        output.append([nums[i],nums[j],nums[k]])
        output.sort()
        output = list(k for k,_ in groupby(output))
        return output

sol = Solution()
startTime = dt.now()
print(sol.threeSum(test_str))
time1 = dt.now() - startTime