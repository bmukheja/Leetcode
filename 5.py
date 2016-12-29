class Solution(object):
    def longestPalindrome(self, s):
        maxLength = 1
        maxPalinStart = 0
        start = 0
        length = len(s)

        #One by one consider every character as the center point of even and odd length palindromes
        for i in range(length):
            #Start with even length palindromes as they have more size and can be checked first easily
            palLength = 0
            left = i
            right = i+1
            while right < length and left >=0:
                #print(left, right)
                if s[left]==s[right]:
                    palLength+=2
                    left -= 1
                    right += 1
                else:
                    break
            if palLength>maxLength:
                maxLength = palLength
                maxPalinStart = left+1

            #Now for odd length palindromes
            if i>0:
                palLength = 1
                left = i - 1
                right = i + 1
                while right < length and left >=0:
                    if s[left]==s[right]:
                        palLength+=2
                        left -= 1
                        right += 1
                    else:
                        break
                if palLength>maxLength:
                    maxLength = palLength
                    maxPalinStart = left+1
        return s[maxPalinStart:maxPalinStart+maxLength]

solution = Solution()
print(solution.longestPalindrome(['b','a','b','a','d']))

