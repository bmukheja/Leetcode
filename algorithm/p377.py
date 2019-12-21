from typing import List

class Solution:
    def combinationSum4(self, nums: List[int], target: int) -> int:
        """
        # Slower solution -
        Backtrack and try to reach to zero

        #Faster -
        Apply memoization to the above
            or
        Create a dp array of length target+1, each number < target can be reached in 1 step from each number2 before it
        by the formula number2 = number - k, for all k in nums. This way for each number2, go through all the k in nums,
        add the answer for reaching number2 as target to number as target
        """
        dp = [0]*(target+1)
        dp[0] = 1
        nums.sort()
        for index in range(target):
            for val in nums:
                if index+val<=target:
                    dp[index+val]+=dp[index]
        return dp[target]



print(Solution().combinationSum4(nums=[1,2,3],target=4))

