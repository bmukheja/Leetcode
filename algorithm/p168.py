import math
class Solution:
    def convertToTitle(self, n: int) -> str:
        n_chars = round(math.log(n,26))
        output = [chr(65+ (n-1)%26)]
        while n_chars:
            n = n//26
            output.append(chr(65+ (n-1)%26))
            n_chars-=1
        return ''.join(output[::-1])