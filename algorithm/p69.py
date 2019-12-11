class Solution:
    def mySqrt(self, x: int) -> int:
        if x ==0:
            return 0
        if x<4:
            return 1
        if x<9:
            return 2
        if x<16:
            return 3
        start,end = 0,x
        while end>start:
            mid = (start+end)//2
            if mid**2==x:
                return mid
            elif mid**2<x:
                start = mid+1
            else:
                end = mid
        while end**2>x:
            end-=1
        return end