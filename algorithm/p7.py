INT_MAX = (2 ** 31 - 1) // 10


class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        x = int(x)
        rev = 0
        if x<0:
            neg = -1
        else:
            neg = 1
        x = abs(x)
        print(INT_MAX)
        while x:
            pop = x % 10
            x //= 10
            if (rev > INT_MAX) or (rev == INT_MAX and pop > 7):
                return 0
            if (rev < -INT_MAX) or (rev == INT_MAX and pop > 8):
                return 0
            rev = rev * 10 + neg*pop
        return rev
