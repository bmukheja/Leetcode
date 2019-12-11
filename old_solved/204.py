class Solution(object):
    def countPrimes(self, n):
        if n < 2:
            return 0
        else:
            lst = [i for i in range(2, n)]
            for i in lst:
                for j in range(i, n, i):
                    if j in lst:
                        lst.remove(j)
            return len(lst)


class Solution(object):
    def countPrimes(self, n):
        lst = [1 for i in range(n)]
        for i in range(1,n/2+1):
            while


solution = Solution()
print(solution.countPrimes(3))