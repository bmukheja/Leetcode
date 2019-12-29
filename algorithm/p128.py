from typing import List

class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums_set = set(nums)
        longest_streak = 0
        for num in nums:
            if num-1 not in nums_set:
                cur_num = num
                cur_streak = 0

                while cur_num in nums_set:
                    cur_num+=1
                    cur_streak+=1
                longest_streak = max(longest_streak,cur_streak)
        return longest_streak


print(Solution().longestConsecutive([100, 4, 200, 1, 3, 2]))