class Solution(object):
    def findPairs(self,s, array):
        from collections import Counter
        c = Counter(array)
        output = []
        for item in c:
            if s-item in c and c[item]!=0:
                if item!= s/2:
                    output+= ([(item,s-item)]*(c[item]*c[s-item]))
                    c[item],c[s-item]=0,0
                elif item == s/2:
                    import math
                    output+=([(item,item)]*math.factorial(c[item]))
                    c[item]=0
        return output


s = Solution()
print(s.findPairs(7,[2,3,2,4,3,5]))