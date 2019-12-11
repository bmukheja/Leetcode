class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        c = 1
        for i in range(len(digits)-1,0,-1):
            s = digits[i] + c
            if s == 10:
                digits[i] = 0
                c = 1
            else:
                digits[i] = s
                c = 0
        s = digits[0]+c
        if s == 10:
            digits[0] = 0
            digits = [1]+digits
        else:
            digits[0] = s
        return digits