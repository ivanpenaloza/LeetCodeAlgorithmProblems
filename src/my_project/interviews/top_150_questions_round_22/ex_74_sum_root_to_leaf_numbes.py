from typing import List, Union, Collection, Mapping, Optional
from abc import ABC, abstractmethod

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def sumNumbers(self, root: TreeNode) -> int:
        """
        Calculate sum of all root-to-leaf numbers using DFS.
        
        Time Complexity: O(n) where n is the number of nodes
        Space Complexity: O(h) where h is the height (recursion stack)
        """
        def dfs(node, current_num):
            if not node:
                return 0
            
            # Build the number by multiplying previous by 10 and adding current digit
            current_num = current_num * 10 + node.val
            
            # If leaf node, return the complete number
            if not node.left and not node.right:
                return current_num
            
            # Recursively process left and right subtrees
            return dfs(node.left, current_num) + dfs(node.right, current_num)
        
        return dfs(root, 0)
    