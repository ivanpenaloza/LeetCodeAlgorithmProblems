from typing import List, Union, Collection, Mapping, Optional
from abc import ABC, abstractmethod

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def flatten(self, root: Optional[TreeNode]) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        if not root:
            return
        
        current = root
        
        while current:
            if current.left:
                # Find the rightmost node in the left subtree
                rightmost = current.left
                while rightmost.right:
                    rightmost = rightmost.right
                
                # Save the current right subtree
                # Connect it to the rightmost node of left subtree
                rightmost.right = current.right
                
                # Move the left subtree to the right
                current.right = current.left
                current.left = None
            
            # Move to the next node
            current = current.right