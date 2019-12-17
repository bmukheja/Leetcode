class Solution:
    def getSum(self, a: int, b: int) -> int:
        # add = xor gate, carry = and gate
        # But in python the integer length is infinite so we need a mask to curb that length
        MAX = 0x7FFFFFFF
        MIN = 0x80000000
        mask = 0xFFFFFFFF

        while b!=0:
            # 6 gets different bits, & gets the double 1s, << moves carry
            a,b = (a ^ b) & mask, ((a & b) << 1) & mask
        return a if a<=MAX else ~(a ^ mask)


print(Solution().getSum(1,2))
print(Solution().getSum(-2,3))