from operator import attrgetter


class Solution:
    # @param a list of ListNode
    # @return a ListNode
    def mergeKLists(self, lists):

        newList = None
        endNode = None
        toSortList = []
        while len(lists) > 0:
            lists = [x for x in lists if x != None]
            for i in range(len(lists)):
                list = lists[i]

                toSortList.append(list)
                lists[i] = list.next
                list.next = None
        toSortList = sorted(toSortList, key=attrgetter('val'))
        for list in toSortList:
            if not newList:
                newList = list
                endNode = newList
            else:
                endNode.next = list
                endNode = list
        return newList

sol = Solution()
print(sol.mergeKLists([[1]]))