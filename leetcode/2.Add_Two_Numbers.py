"""
You are given two non-empty linked lists representing two non-negative integers. The digits are stored in reverse order and each of their nodes contain a single digit. Add the two numbers and return it as a linked list.

You may assume the two numbers do not contain any leading zero, except the number 0 itself.

Example

Input: (2 -> 4 -> 3) + (5 -> 6 -> 4)
Output: 7 -> 0 -> 8
Explanation: 342 + 465 = 807.

"""

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

# constraints : carry over 
# Idea 1 : enumerate the lists from smaller to bigger , add the numbers and then reverse the list, keep a carry for each step

class Solution:
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """

        carry = 0
        listofNodes = []
        while(True):
            a = b = 0
            if l1:
                a = l1.val
                l1 = l1.next
            if l2:
                b = l2.val
                l2 = l2.next
            total = a + b + carry
            if total >= 10:
               carry = 1
               total = total % 10
            else:
                carry = 0
            
 
            listofNodes.append(ListNode(total))
            
            if l1 == None and l2 == None:
                break
        if carry:
            listofNodes.append(ListNode(carry))
        for i in range(len(listofNodes)-1):
            listofNodes[i].next = listofNodes[i+1]
        return listofNodes[0]              
            
