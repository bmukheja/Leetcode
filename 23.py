# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def minInLists(self, lists):
        mini = 0
        for lList in lists:
            if lList.val < mini:
                mini = lList.val
                if lList.next != None:
                    lList = lList.next
                else:
                    lists.remove(lList)
        return mini

    def mergeKLists(self, lists):
        """
        :type lists: List[ListNode]
        :rtype: ListNode
        """
        lists = [x for x in lists if x != None]
        if not lists:
            return []
        output = ListNode(self.minInLists(lists))
        new = output
        while lists:
            temp = self.minInLists(lists)
            new.next = temp
            new = temp
        return output

