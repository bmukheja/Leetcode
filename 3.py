class Solution(object):
    def lengthOfLongestSubstring(self, s):
        lst = []
        max_len = 0
        for i in s:
            if i in lst:
                max_len = max(max_len,len(lst))
                del lst[:]
            lst.append(i)
        max_forward =  max(max_len,len(lst))
        for i in s[::-1]:
            if i in lst:
                max_len = max(max_len,len(lst))
                del lst[:]
            lst.append(i)
        max_backward =  max(max_len,len(lst))
        return max(max_backward,max_forward)

solution = Solution()
print(solution.countPrimes(3))