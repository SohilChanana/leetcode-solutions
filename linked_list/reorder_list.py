# Leetcode Problem 143: Reorder List
# https://leetcode.com/problems/reorder-list/

# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution(object):
    def reorderList(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: None Do not return anything, modify head in-place instead.
        """
        slow, fast = head, head.next

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        
        secondHead = slow.next
        slow.next = None
        prev = None
        while secondHead:
            temp = secondHead.next
            secondHead.next = prev
            prev = secondHead
            secondHead = temp
        
        firstHead, secondHead = head, prev
        while secondHead:
            temp1, temp2 = firstHead.next, secondHead.next
            firstHead.next = secondHead
            secondHead.next = temp1
            firstHead, secondHead = temp1, temp2
        return head

        