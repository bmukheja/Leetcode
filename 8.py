class Solution(object):
    def myAtoi(self, str):
        """
        :type str: str
        :rtype: int
        """
        if len(str)==0:
            return 0
        str = "".join(str.split())
        sign = ''
        if str[0] == '-':
            sign = '-'
            str = str[1:]
        elif str[0]=='+':
            str = str[1:]
            pass
        #str = "".join(str.split('+-'))
        #str = "".join(str.split('+'))
        from itertools import takewhile
        try:
            output = int(''.join([sign]+[x for x in takewhile(lambda x: 48<= ord(x) < 58, str)]))
        except:
            return 0
        return output

sol = Solution()
print(sol.myAtoi(''))