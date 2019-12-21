from typing import List

class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        """
        #Create a dp array of the length of string s + 1. For each word till where it can be completed using words from dict
        mark it as positive else negative
        """
        dp = [False]*(len(s)+1)
        dp[0] = True
        wordDict = set(wordDict)
        for index in range(len(s)):
            if dp[index] == True:
                for word in wordDict:
                    if s[index:].startswith(word):
                        dp[index+len(word)] = True
        return dp[len(s)]

print(Solution().wordBreak(s="leetcode",wordDict= ["leet", "code"]))
print(Solution().wordBreak(s = "applepenapple", wordDict = ["apple", "pen"]))
print(Solution().wordBreak(s = "catsandog", wordDict = ["cats", "dog", "sand", "and", "cat"]))