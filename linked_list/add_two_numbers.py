# Leetcode Problem 2: Add Two Numbers
# https://leetcode.com/problems/add-two-numbers/

# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: Optional[ListNode]
        :type l2: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        num1 = 0
        i = 0
        while l1 != None:
            num1 += l1.val * (10 ** i)
            i += 1
            l1 = l1.next
        num2 = 0
        i = 0
        while l2 != None:
            num1 += l2.val * (10 ** i)
            i += 1
            l2 = l2.next

        total = num1 + num2
        result = ListNode()
        head = result
        while total > 0:
            digit = total % 10
            total =  total // 10
            result.val = digit
            if total > 0:
                result.next = ListNode()
                result = result.next
        return head