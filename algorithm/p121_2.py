import sys
from typing import List

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if not prices or len(prices) == 1:
            return 0
        maxprofit = 0
        minprice = sys.maxsize
        for price in prices:
            if price<minprice:
                minprice = price
            elif price - minprice>maxprofit:
                maxprofit = price - minprice
        return maxprofit

