from typing import List

class Solution:
    def grayCode(self, n: int) -> List[int]:
        """Create a set of done ints, walk through the int, loop thorugh the back to the fron, flip the bit and run the code on the new int again, add it to list, otherwise backtrack and change another bit. Do this till length of output is 2**n"""
        done = set([0])
        output = list([0])

        def flip_k_bit(number, k):
            return (number ^ 1 << k)

        def helper(number):
            if len(output) == 2**n:
                return output
            for k in range(n):
                num = flip_k_bit(number,k)
                if num not in done:
                    output.append(num)
                    done.add(num)
                    helper(num)
            return
        helper(0)
        return output

print(Solution().grayCode(18))