# Leetcode Problem 206: Reverse Linked List
# https://leetcode.com/problems/reverse-linked-list/

# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution(object):
    def reverseList(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: Optional[ListNode]
        """

        ################ Iterative Solution ################
        
        prev = None
        while head:
            temp = head.next
            head.next = prev
            prev = head
            head = temp

        return prev