from typing import List
import sys

class Solution1:
    def coinChange(self, coins: List[int], amount: int) -> int:
        #Brute force solution(Backtracking) - Time Limit Exceeded
        # Sort the combination list in desc order
        # One by one pick a coin from the combinations, and add to amount
        # If the amount if less than desired, add more of the same
        # If the amount is same, compare to global answer
        # If the amount is more, return and try the next lowest denomination
        self.min_coins = sys.maxsize
        self.amount = amount
        coins.sort(reverse=True)

        self.helper(0,0, coins)
        if self.min_coins == sys.maxsize:
            return -1
        else:
            return self.min_coins

    def helper(self, cur_coins, cur_sum, coins):
        if cur_sum == self.amount:
            if cur_coins < self.min_coins:
                self.min_coins = cur_coins
                return
        elif cur_sum > self.amount:
            return
        else:
            for coin in coins:
                self.helper(cur_coins + 1, cur_sum + coin, coins)

class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        # Create a dp array
        # Subproblem = for each amount k, I can jump to next few amounts using 1 coin of each denomination
        # Stop when this is more than the amount
        coins.sort(reverse=True)
        dp = [-1]*(amount+1)
        dp[0] = 0
        for a in range(amount):
            if dp[a]!= -1:
                for coin in coins:
                    if a+coin<=amount:
                        if dp[a+coin] == -1:
                            dp[a+coin] = dp[a]+1
                        else:
                            dp[a+coin] = min(dp[a]+1,dp[a+coin])
        return dp[amount]

print(Solution().coinChange([1,2,5],11))
