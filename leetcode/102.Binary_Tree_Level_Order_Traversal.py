"""
Given a binary tree, return the level order traversal of its nodes' values. (ie, from left to right, level by level).

For example:
Given binary tree [3,9,20,null,null,15,7],
    3
   / \
  9  20
    /  \
   15   7
return its level order traversal as:
[
  [3],
  [9,20],
  [15,7]
]
"""

class Solution:
    def levelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        
        if root is None:
            return [] 
        queue = []
        queue.append((0, root))
        result = [[]]
        while(len(queue) > 0):
            level, node = queue.pop(0)            
            if node.left is not None:               
                queue.append((level + 1, node.left))           
            if node.right is not None:
                queue.append((level + 1, node.right))
            if len(result) <= level:
                result.append([])
            result[level].append(node.val)
        
        return result
