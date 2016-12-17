# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x[0]
        self.next = None
        if len(x)>1:
            new_node = ListNode(x[1:])
            self.next = new_node

    def __repr__(self):
        lst = []
        temp = self
        while(temp.next!=None):
            lst.append(temp.val)
            temp = temp.next
        return str(lst)

class Solution(object):
    def addTwoNumbers(self, l1, l2):
        carry_forward = 0
        carry_forward, val = divmod(l1.val + l2.val + carry_forward, 10)
        new_node = third = ListNode(val)
        l1 = l1.next
        l2=l2.next
        while (l1 or l2 or carry_forward):
            val1 = val2 = 0
            if l1:
                val1 = l1.val
                l1 = l1.next
            if l2:
                val2 = l2.val
                l2 = l2.next
            carry_forward, val = divmod(val1 + val2 + carry_forward,10)
            new_node.next = ListNode(val)
            new_node = new_node.next
        return third


solution = Solution()
print(solution.addTwoNumbers([2,4,3],[5,6,4]))
