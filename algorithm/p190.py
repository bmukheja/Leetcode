class Solution:
    def reverseBits(self, n: int) -> int:
        output = 0
        for i in range(32):
            temp = (1 << (31 - i)) if (n >> i & 1) == 1 else 0
            output = output | temp
        return output

print(Solution().reverseBits(0b00000010100101000001111010011100))