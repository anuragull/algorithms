"""
Merge two sorted linked lists and return it as a new list. The new list should be made by splicing together the nodes of the first two lists.

Example:

Input: 1->2->4, 1->3->4
Output: 1->1->2->3->4->4

"""

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def mergeTwoLists(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        
        if l1 is None and l2 is None:
            return None
        if l1 is None:
            return l2
        if l2 is None:
            return l1
        
        
        # set the first 
        if l1.val < l2.val :
            root = ListNode(l1.val)
            l1 = l1.next
        else:
            root = ListNode(l2.val)
            l2 = l2.next
        first = root
        while(l1 or l2):
            
            if l1 and l2:
                if l1.val < l2.val :
                    node = ListNode(l1.val)
                    l1 = l1.next
                else:
                    node = ListNode(l2.val)
                    l2 = l2.next
                root.next = node
                root = node
            elif l1:
                node = ListNode(l1.val)
                l1 = l1.next
                root.next = node
                root = node
            elif l2:
                node = ListNode(l2.val)
                l2 = l2.next
                root.next = node
                root = node
        return first
        
        
