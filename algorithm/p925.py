class Solution:
    def isLongPressedName(self, name: str, typed: str) -> bool:
        """Create two counters, loop through both strings,
        increase the first counter only if the next character in both the counters
        is the same else increase the second counter only"""
        if len(name) > len(typed):
            return False
        i, j = 0, 0
        while i < len(name):
            if j==len(typed):
                return False
            if typed[j] == name[i]:
                j+=1
                i+=1
            elif typed[j] == typed[j-1]:
                while j < len(typed) and typed[j] == typed[j - 1]:
                    j += 1
            else:
                return False
        return True

import sys
name = sys.argv[1]
typed = sys.argv[2]
print(Solution().isLongPressedName(name,typed))