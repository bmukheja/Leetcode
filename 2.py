# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x[0]
        if len(x)>1:
            for item in x[1:]:
                self.next = ListNode(item,self)

    def __init__(self, x, prevNode):
        self.val = x
        self.next = prevNode


class Solution(object):
    def addTwoNumbers(self, l1, l2):
        first = ListNode(l1)
        second = ListNode(l2)
        sum = first.val + second.val
        new_node = ListNode(sum % 10)
        third = new_node
        carry_forward = int(sum / 10)
        while (first.next != None and second.next != None):
            first = first.next
            second = second.next
            sum = first.val + second.val + carry_forward
            new_node = ListNode(sum % 10, new_node)
            carry_forward = int(sum / 10)
        if (first.next == None and second.next != None):
            while (second.next != None):
                second = second.next
                sum = second.val + carry_forward
                new_node = ListNode(sum % 10, new_node)
                carry_forward = int(sum / 10)
        elif (first.next != None and second.next == None):
            while (first.next != None):
                first = first.next
                sum = second.val + carry_forward
                new_node = ListNode(sum % 10, new_node)
                carry_forward = int(sum / 10)
        elif (first.next == None and second.next == None):
            return third


solution = Solution()
print(solution.addTwoNumbers([2,4,3],[5,6,4]))
