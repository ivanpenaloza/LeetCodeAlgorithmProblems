from typing import List, Union, Collection, Mapping, Optional
from abc import ABC, abstractmethod

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        self.max_sum = float('-inf')
        
        def dfs(node: Optional[TreeNode]) -> int:
            """
            Returns the maximum path sum that can be extended to the parent.
            Updates self.max_sum with the maximum path sum through this node.
            """
            if not node:
                return 0
            
            # Get maximum contribution from left and right subtrees
            # Use max with 0 to ignore negative paths
            left_max = max(0, dfs(node.left))
            right_max = max(0, dfs(node.right))
            
            # Maximum path sum through this node (can't be extended upward)
            path_through_node = node.val + left_max + right_max
            
            # Update global maximum
            self.max_sum = max(self.max_sum, path_through_node)
            
            # Return maximum path that can be extended to parent
            # Can only choose one direction (left or right)
            return node.val + max(left_max, right_max)
        
        dfs(root)
        return self.max_sum