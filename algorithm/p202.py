class Solution(object):
    def isHappy(self, n):
        """
        :type n: int
        :rtype: bool
        """
        aSet = set([n])
        while n!=1:
            total = 0
            while n:
                total += (n%10)**2
                n = n//10
            n = total
            if n in aSet:
                return False
            else:
                aSet.add(n)
        return True