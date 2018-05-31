"""
Reverse a singly linked list.

Example:

Input: 1->2->3->4->5->NULL
Output: 5->4->3->2->1->NULL
Follow up:

A linked list can be reversed either iteratively or recursively. Could you implement both?


"""

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if head is None:
            return head
        # set prev as None
        prev = None
        while head is not None:
            # get the next one temp = b
            temp = head.next
            # set the next one as 
            head.next = prev
            # prev is a, b->a
            prev = head
            # set  
            head = temp
        # return prev
        return prev
            
