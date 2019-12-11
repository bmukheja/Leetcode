import random
class Solution(object):
    def generateParenthesis(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        combinations = []
        def helper(cur,left,right):
            if len(cur)==2*n:
                combinations.append(cur)
                return
            if left:
                helper(cur+'(',left-1,right)
            if right>left:
                helper(cur+')',left,right-1)

        helper('',n,n)
        return combinations