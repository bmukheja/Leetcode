class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        from collections import defaultdict
        d = defaultdict(list)
        for item in strs:
            if item != "":
                d[tuple(sorted(item))].append(item)
        output = [list for key,list in d]
        return output

