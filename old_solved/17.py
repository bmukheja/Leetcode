class Solution(object):
    def matMultiply(self, matFirst, matSecond):
        output = []
        for item1 in matFirst:
            for item2 in matSecond:
                output.append(item1+item2)
        return output

    def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """
        defDict = {'2':['a','b','c'],'3':['d','e','f'],'4':['g','h','i'],'5':['j','k','l'],'6':['m','n','o'],'7':['p','q','r','s'],'8':['t','u','v'],'9':['w','x','y','z'],'*':['+'],'0':['_']}
        output = []
        try:
            output = defDict[digits[0]]
        except:
            pass
        i = 1
        while i<len(digits):
            output = self.matMultiply(output,defDict[digits[i]])
            i+=1
        return output

sol = Solution()
print(sol.letterCombinations('99'))