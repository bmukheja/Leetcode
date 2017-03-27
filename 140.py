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
        wb = [None]*(l+1) #Initialise all values as false
        for i in range(1,l+1):
            #If wb[i] is false, then check if the currect prefix can make it true.
            #Current prefix is "s[:i]
            if s[:i] in wordDict:
                if not wb[i]:
                    wb[i] = [[i]]
                else:
                    wb[i] += [[i]]

            #wb[i] is true, then check for all the substrings starting from
            #(i+1)th character and store their results.
            if wb[i]:

                for j in range(i+1,l+1):
                    #Update wb[j] if it is false and can be updated
                    #Note the string checked in the dictionary is s[i:j]
                    if s[i:j] in wordDict:
                        if not wb[j]: wb[j]=[item+[j] for item in wb[i]]
                        else:
                            wb[j] += [item + [j] for item in wb[i]]


        #If we tried all prefixes and none of them worked
        print wb
        return 1#[" ".join(array) for array in wb if not array]





sol = Solution()
print sol.wordBreak("aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaab",["a","aa","aaa","aaaa","aaaaa","aaaaaa","aaaaaaa","aaaaaaaa","aaaaaaaaa","aaaaaaaaaa"])
