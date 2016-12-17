class Solution(object):
    def hammingWeight(self, n):
        if n==0:
            return 0
        else:
            from math import log
            s = int(log(n,2))+1
            count = 0
            for i in range(s):
                count+= (n>>i)%2
            return count