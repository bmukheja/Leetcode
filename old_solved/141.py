class Solution(object):
    def hasCycle(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        a,b = head,head
        if head: b = head.next
        if a and b and a == b: return True
        while a and b:
            try:
                a = a.next
            except:
                a = None
            try:
                b = (b.next).next
            except:
                b = None
            if (a and b and (a == b)):
                return True
        return False