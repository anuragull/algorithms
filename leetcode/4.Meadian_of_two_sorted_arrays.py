"""
There are two sorted arrays nums1 and nums2 of size m and n respectively.

Find the median of the two sorted arrays. The overall run time complexity should be O(log (m+n)).

Example 1:
nums1 = [1, 3]
nums2 = [2]

The median is 2.0
Example 2:
nums1 = [1, 2]
nums2 = [3, 4]

The median is (2 + 3)/2 = 2.5

"""

# Constraint : 
# idea : keep two balanced heaps min and max heaps 

import heapq
import itertools
class Solution:
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        min_heap = []
        max_heap = []
        
        for x in itertools.chain(nums1, nums2):
            heapq.heappush(max_heap, -heapq.heappushpop(min_heap, x))
            # ensure the heaps are balanced
            if len(max_heap) > len(min_heap):
                heapq.heappush(min_heap, -heapq.heappop(max_heap))
        return float(0.5 * (min_heap[0] + (-max_heap[0]))) if len(max_heap) == len(min_heap) else float(min_heap[0])
