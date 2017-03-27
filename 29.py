class Solution(object):
    def divide(self, dividend, divisor):
        """
        :type dividend: int
        :type divisor: int
        :rtype: int
        """
        import sys
        i = 0
        if divisor == 0:
            return sys.maxint
        elif dividend == 0:
            return 0
        else:
            try:
                num,den = abs(dividend),abs(divisor)
                for j in range(0, num, den):
                    i += 1
                if (dividend < 0 and divisor > 0) or (dividend > 0 and divisor < 0):
                    i = -i
                return i
            except:
                return sys.maxint

s = Solution()
print(s.divide(1,-1))