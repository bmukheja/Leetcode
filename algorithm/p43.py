class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        # Multiply numbers using relation (10a+b)*(10c+d) = 100ac+10(ad+bc)+bd
        if num1 == "0" or num2 == "0":
            return "0"
        if num1 == "1":
            return num2
        elif num2 == "1":
            return num1

        #Add special condition for numbers ending with 0

        ans = "0"
        ord_zero = 48
        if len(num2) == 1:
            for i in range(ord(num2)-ord_zero):
                ans = self.add(num1,ans)
            return ans
        elif len(num1) == 1 and len(num2) != 1:
            for i in range(ord(num1)-ord_zero):
                ans = self.add(num2,ans)
            return ans

        #Now use the above equation = 100ac + 10(ad+bc) + bd
        a = num1[:-1]
        c = num2[:-1]
        b = num1[-1]
        d = num2[-1]
        first_value = self.multiply(a,c) + "00" #Two zeros for multiplying by hundred, a quick hack
        second_value = self.add(self.multiply(a,d), self.multiply(b,c)) + "0"
        third_value = str((ord(b) - 48) * (ord(d) - 48))

        return self.add(first_value, self.add(second_value, third_value))

    def add(self, n1: str, n2: str) -> str:
        if len(n1)==0 or n1=="0":
            return n2
        elif len(n2)==0 or n2 == "0":
            return n1
        ans = []
        carry = 0
        s = 0
        n1_length = len(n1)
        n2_length = len(n2)
        while n1_length and n2_length:
            s = ord(n1[n1_length-1]) + ord(n2[n2_length-1]) - 96 + carry
            carry = s//10
            s = s%10
            ans.append(str(s))
            n1_length -=1
            n2_length -=1

        if n1_length==0 and n2_length==0:
            if carry:
                ans.append(str(carry))
            return ''.join(ans[::-1])

        elif n1_length:
            rem = n1[:n1_length]
        else:
            rem = n2[:n2_length]

        if not carry:
            ans.extend(rem[::-1])
        else:
            for item in rem[::-1]:
                s = ord(item) - 48 + carry
                carry = s//10
                s = s%10
                ans.append(str(s))
            if carry:
                ans.append(str(carry))
        return ''.join(ans[::-1])



print(Solution().multiply("2","3"))
print(Solution().multiply("123","456"))
print(Solution().multiply("2","0"))