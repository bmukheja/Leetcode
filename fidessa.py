#Find a character that repeats in a string, find the first such character. e.g. 'abcba', output = 'a'

class Solution(object):
    def findRepeat(self, str):
        from collections import Counter
        c = Counter(str)
        for char in str:
            if c[char]>1:
                return char


a = Solution()
print(a.findRepeat('abcba'))


