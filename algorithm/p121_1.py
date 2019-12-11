import sys

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        minprice = sys.maxsize
        maxprofit = 0
        for i in prices:
            if i < minprice:
                minprice = i
            elif (i - minprice) > maxprofit:
                maxprofit = i - minprice
        return maxprofit