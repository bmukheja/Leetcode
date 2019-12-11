class Solution(object):
    def addDigits(self, num):
        """
        :type num: int
        :rtype: int
        """
        if not num:
            return 0
        l = len(str(num))
        digits = [(num//10**i)%10 for i in range(l)]
        i = 0
        output = 0
        while i<l:
            output += digits[i]
            while len(str(output))>1:
                output = output%10 + output//10
            i+=1
        return output