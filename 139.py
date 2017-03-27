class Solution(object):
    def wordBreak(self, s, wordDict):
        """
        :type s: str
        :type wordDict: List[str]
        :rtype: bool
        """
        l = len(s)
        if l==0: return True
        #Create DP table to store results of subproblems. The value wb[i]
        #will be true if str[0..i-1] can be segmented into dictionary words,
        #otherwise false.
        wb = bytearray(l+1) #Initialise all values as false
        for i in range(1,l+1):
            #If wb[i] is false, then check if the currect prefix can make it true.
            #Current prefix is "s[:i]
            if not wb[i] and s[:i] in wordDict: wb[i] = True

            #wb[i] is true, then check for all the substrings starting from
            #(i+1)th character and store their results.
            if wb[i]:

                #If we reached the last prefix
                if i==l: return True
                for j in range(i+1,l+1):

                    #Update wb[j] if it is false and can be updated
                    #Note the string checked in the dictionary is s[i:j]
                    if not wb[j] and s[i:j] in wordDict: wb[j]=True

                    #If we reached the last character
                    if j==l and wb[j]: return True

        #If we tried all prefixes and none of them worked
        return False

    def wordBreak2(self,s, wordDict):
        trie = Trie(wordDict)
        i = 0
        l = len(s)
        while s[i] in trie


class Trie():
    def __init__(self,*words):


class Node():
    next = list()
    def __init__(self,val, next):




sol = Solution()
print sol.wordBreak("aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaab",["a","aa","aaa","aaaa","aaaaa","aaaaaa","aaaaaaa","aaaaaaaa","aaaaaaaaa","aaaaaaaaaa"])
