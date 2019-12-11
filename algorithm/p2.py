# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        c = 0
        t1 = l1
        t2 = l2
        prev1 = None
        prev2 = None

        while t1 and t2:
            prev1 = t1
            t1.val = t1.val + t2.val + c
            if t1.val > 9:
                t1.val = t1.val % 10
                c = 1
            else:
                c = 0
            t1 = t1.next
            t2 = t2.next
        if t2 and not t1:
            prev1.next = t2
            while c and t2:
                t2.val += c
                if t2.val > 9:
                    c = 1
                else:
                    c = 0
                t2 = t2.next
        if t1 and not t2:
            while c and t1:
                t1.val += c
                if t1.val > 9:
                    c = 1
                else:
                    c = 0
                prev1 = t1
                t1 = t1.next
        if not t1 and not t2 and c:
            prev1.next = ListNode(c)
        return l1


