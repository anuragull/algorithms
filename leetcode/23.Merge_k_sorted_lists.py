"""
Merge k sorted linked lists and return it as one sorted list. Analyze and describe its complexity.

Example:

Input:
[
  1->4->5,
  1->3->4,
  2->6
]
Output: 1->1->2->3->4->4->5->6
"""
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None


# constraints : check for null
# idea :
# 1.  main 'k' list of elements at each index, get the minimun from it, get the next element for this 
# Idea two use a counter (hash table)
# Idea maintain heap? 
import collections
class Solution:
    def mergeKLists(self, lists):
        """
        :type lists: List[ListNode]
        :rtype: ListNode
        """
        counter = collections.Counter()
        for i in lists:
            while i:
                counter[i.val] += 1
                i = i.next
        start = None
        for key in sorted(counter):
            val = counter[key]
            for i in range(val):                
                node = ListNode(key)                
                if start:                    
                    prev.next = node
                else:
                    start = node
                prev = node
        return start
