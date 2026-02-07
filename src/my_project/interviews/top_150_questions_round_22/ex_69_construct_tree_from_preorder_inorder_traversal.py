from typing import List, Union, Collection, Mapping, Optional
from abc import ABC, abstractmethod

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        # Create a hashmap for quick lookup of indices in inorder
        inorder_map = {val: idx for idx, val in enumerate(inorder)}
        self.preorder_idx = 0
        
        def build(left: int, right: int) -> Optional[TreeNode]:
            # Base case: no elements to construct the tree
            if left > right:
                return None
            
            # Pick the current root from preorder
            root_val = preorder[self.preorder_idx]
            root = TreeNode(root_val)
            
            # Move to the next element in preorder
            self.preorder_idx += 1
            
            # Find the index of root in inorder to split left and right subtrees
            inorder_idx = inorder_map[root_val]
            
            # Build left subtree (all elements before root in inorder)
            root.left = build(left, inorder_idx - 1)
            
            # Build right subtree (all elements after root in inorder)
            root.right = build(inorder_idx + 1, right)
            
            return root
        
        return build(0, len(inorder) - 1)